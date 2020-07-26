from flask import Flask, request, render_template, jsonify
from flask_wtf import FlaskForm
from flask.logging import create_logger
from wtforms import HiddenField, IntegerField, SubmitField
from wtforms.validators import NumberRange
from tic_tac_toe_engine import TicTacToeEngine
import logging
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess-123'
LOG = create_logger(app)
LOG.setLevel(logging.INFO)


class PlayForm(FlaskForm):
    """
    Creates the simple form to play tic-tac-toe.
    """
    the_0_0 = HiddenField('the_0_0')
    the_0_1 = HiddenField('the_0_1')
    the_0_2 = HiddenField('the_0_2')
    the_1_0 = HiddenField('the_1_0')
    the_1_1 = HiddenField('the_1_1')
    the_1_2 = HiddenField('the_1_2')
    the_2_0 = HiddenField('the_2_0')
    the_2_1 = HiddenField('the_2_1')
    the_2_2 = HiddenField('the_2_2')

    i = IntegerField('i', validators=[NumberRange(min=0, max=2, message='Out of Range')])
    j = IntegerField('j', validators=[NumberRange(min=0, max=2, message='Out of Range')])
    submit = SubmitField('Play')


def query_tic_tac_toe_engine(state):
    payload = state
    res = requests.post('http://0.0.0.0:8080/tic_tac_toe_engine', json=payload, headers={'Content-Type': 'application/json'})
    res_json = res.json()
    return res_json['the_play']


@app.route("/", methods=['GET', 'POST'])
def home():
    form = PlayForm()
    state = {i: {j: getattr(form, f'the_{i}_{j}').data for j in range(0, 3)} for i in range(0, 3)}
    already_play = True
    if form.validate_on_submit():
        print("Is valid")
        # Upon submitting the form, let's update it from the player's form
        print(f"Player's move: ({form.i.data},{form.j.data})")
        user_input_i = int(form.i.data)
        user_input_j = int(form.j.data)
        # Check that the input is valid, i.e., that it hasn't been played before.
        if state[user_input_i][user_input_j] == '':
            already_play = False
            # Update the state with the user's input.
            state[user_input_i][user_input_j] = 'P'
            # Update the form (and hence, the table layout) with the user's input.
            hidden_field = getattr(form, f'the_{user_input_i}_{user_input_j}')
            hidden_field.data = 'P'

            # Let the engine play
            the_engines_play = query_tic_tac_toe_engine(state)
            if the_engines_play is not None:
                # Update the state with the user's input
                state[the_engines_play[0]][the_engines_play[1]] = 'C'
                # Update the form (and hence, the table layout) with the engine's output.
                hidden_field = getattr(form, f'the_{the_engines_play[0]}_{the_engines_play[1]}')
                hidden_field.data = 'C'

        # Log the current state, for debugging purposes.
    LOG.info(f"state = {state}")

    return render_template('play.html',
                           state=state,
                           already_play=already_play,
                           title='Sign In',
                           form=form)


@app.route("/tic_tac_toe_engine", methods=['POST'])
def tic_tac_toe_engine():
    json_payload = request.json
    LOG.info(f"JSON payload: {json_payload}")
    the_tic_tac_toc_engine = TicTacToeEngine(json_payload)
    json_response = jsonify({'the_play': the_tic_tac_toc_engine.play()})
    LOG.info(f"JSON response: {json_response}")
    return json_response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
