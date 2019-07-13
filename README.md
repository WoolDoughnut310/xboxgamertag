# xboxgamertag
Python module to get data from www.xboxgamertag.com

## Usage
#### Installation
`pip install xboxgamertag`
#### Simple example
```python
from xboxgamertag import gamertag

user = Gamertag('WoolDoughnut310') # My gamertag is WoolDoughnut310, by the way

# Get my amount of gamerscore
print(user.gamerscore)

# If you want to see how many games I have played in total
print(user.total_games_played)
```
<div id="gamertag">
<dl>
  <dt id="xboxgamertag.Gamertag">
    <em>class </em>
    <code>xboxgamertag.Gamertag</code>
    <span>(</span>
    <em>name</em>
    <span>)</span>
  </dt>
  <dd>
    <p>
      Initializes the Gamertag class and returns an object
    </p>
    <code>BASE_URL = "https://www.xboxgamertag.com"</code>
    <dl>
      <dt id="xboxgamertag.Gamertag.icon">
        <code>icon</code>
        <a href="#xboxgamertag.Gamertag.icon" title="Permalink to this definition">¶</a>
      </dt>
      <dd>
        <p>
          The url to the profile pic of the user<br>Returns <code><a href="https://docs.python.org/3/library/stdtypes.html?highlight=str#str">str</a></code>
        </p>
      </dd>
    </dl>
    <dl>
      <dt id="xboxgamertag.Gamertag.gamertag">
        <code>gamertag</code>
        <a href="#xboxgamertag.Gamertag.gamertag" title="Permalink to this definition">¶</a>
      </dt>
      <dd>
        <p>
          The full name of the user<br>Returns <code><a href="https://docs.python.org/3/library/stdtypes.html?highlight=str#str">str</a></code>
        </p>
      </dd>
    </dl>
    <dl>
      <dt id="xboxgamertag.Gamertag.gamerscore">
        <code>gamerscore</code>
        <a href="#xboxgamertag.Gamertag.gamerscore" title="Permalink to this definition">¶</a>
      </dt>
      <dd>
        <p>
          The amount of gamerscore the user has achieved in total<br>Returns <code><a href="https://docs.python.org/3/library/functions.html?highlight=int#int">int</a></code>
        </p>
      </dd>
    </dl>
    <dl>
      <dt id="xboxgamertag.Gamertag.total_games_played">
        <code>total_games_played</code>
        <a href="#xboxgamertag.Gamertag.total_games_played" title="Permalink to this definition">¶</a>
      </dt>
      <dd>
        <p>
          The total amount of games played by the user<br>Returns <code><a href="https://docs.python.org/3/library/functions.html?highlight=int#int">int</a></code>
        </p>
      </dd>
    </dl>
    <dl>
      <dt id="xboxgamertag.Gamertag.games_completed">
        <code>games_completed</code>
        <a href="#xboxgamertag.Gamertag.games_completed" title="Permalink to this definition">¶</a>
      </dt>
      <dd>
        <p>
          The total amount of games the user has completed<br>Returns <code><a href="https://docs.python.org/3/library/functions.html?highlight=int#int">int</a></code>
        </p>
      </dd>
    </dl>
    <dl>
      <dt id="xboxgamertag.Gamertag.games_played">
        <code>games_played</code>
        <a href="#xboxgamertag.Gamertag.games_played" title="Permalink to this definition">¶</a>
      </dt>
      <dd>
        <p>
          All the games the user has played<br>Returns list of <code><a href="#xboxgamertag.PlayedGame">PlayedGame</a></code> objects
        </p>
      </dd>
    </dl>
  </dd>
</dl>
</div>

<div id="played_game">
<dl>
  <dt id="xboxgamertag.PlayedGame">
    <em>class </em>
    <code>xboxgamertag.PlayedGame</code>
    <span>(</span>
    <em>tr</em>
    <span>)</span>
  </dt>
  <dd>
    <p>
      Initializes the PlayedGame class and returns an object
    </p>
    <dl>
      <dt id="xboxgamertag.PlayedGame.icon">
        <code>icon</code>
        <a href="#xboxgamertag.PlayedGame.icon" title="Permalink to this definition">¶</a>
      </dt>
      <dd>
        <p>
          The url to the profile pic of the game<br>Returns <code><a href="https://docs.python.org/3/library/stdtypes.html?highlight=str#str">str</a></code>
        </p>
      </dd>
    </dl>
    <dl>
      <dt id="xboxgamertag.PlayedGame.title">
        <code>title</code>
        <a href="#xboxgamertag.PlayedGame.title" title="Permalink to this definition">¶</a>
      </dt>
      <dd>
        <p>
          The full name of the game<br>Returns <code><a href="https://docs.python.org/3/library/stdtypes.html?highlight=str#str">str</a></code>
        </p>
      </dd>
    </dl>
    <dl>
      <dt id="xboxgamertag.PlayedGame.total_earned_gamerscore">
        <code>total_earned_gamerscore</code>
        <a href="#xboxgamertag.PlayedGame.total_earned_gamerscore" title="Permalink to this definition">¶</a>
      </dt>
      <dd>
        <p>
          The amount of gamerscore the user has achieved in the game in total<br>Returns <code><a href="https://docs.python.org/3/library/functions.html?highlight=int#int">int</a></code>
        </p>
      </dd>
    </dl>
    <dl>
      <dt id="xboxgamertag.PlayedGame.total_unlocked_achievements">
        <code>total_unlocked_achievements</code>
        <a href="#xboxgamertag.PlayedGame.total_unlocked_achievements" title="Permalink to this definition">¶</a>
      </dt>
      <dd>
        <p>
          The total amount of achievements unlocked by the user in that game<br>Returns <code><a href="https://docs.python.org/3/library/functions.html?highlight=int#int">int</a></code>
        </p>
      </dd>
    </dl>
  </dd>
</dl>
</div>
