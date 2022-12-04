To try and udnerstand the problem, I tried to take the fluff out of the question:

<details><summary><h3>Story</h3></summary>
- Winner gets to pitch their tent closest to the snack tent.</br>
- An elf gives you a list of what hand the enemy will play</br>
- The list contains a second column with unknown significance</br>
</details>
<details><summary><h3>Part Two</h3></summary>
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
</details>

### Main objective
**Win** Rock Paper Scissors by **maximising score**.

#### Understanding score

`calculateScore`
|Score matrix  | (6) Win | (3) Draw | (0) Lose |
|-             |-        |-         |-         |
|(1) Rock      |7        |4         |1         |
|(2) Paper     |8        |5         |2         |
|(3) Scissors  |9        |6         |3         |

`calculateOutcome`
|Turn Outcome|X Rock    |Y Paper    |Z Scissors |
|-           |-         |-          |-          |
|A Rock      |Draw      |Win        |Lose       |
|B Paper     |Lose      |Draw       |Win        |
|C Scissors  |Win       |Lose       |Draw       |
