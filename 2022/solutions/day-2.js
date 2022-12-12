answerTablePart1= {    //decipherScore
    'A X': 4,     // 1     + 3
    'A Y': 8,     // 2     + 6
    'A Z': 3,     // 3     + 
    'B X': 1,     // 4     + 
    'B Y': 5,     // 5     + 
    'B Z': 9,     // 6     + 
    'C X': 7,     // 7     + 
    'C Y': 2,     // 8     + 
    'C Z': 6      // 9     + 
}

answerTablePart2= {   //decipherHand
    'A X': 3,     // 3     + 0
    'A Y': 4,     // 1     + 3
    'A Z': 8,     // 2     + 6
    'B X': 1,     // 1     + 0
    'B Y': 5,     // 2     + 3
    'B Z': 9,     // 3     + 6
    'C X': 2,     // 2     + 0
    'C Y': 6,     // 3     + 3
    'C Z': 7      // 1     + 6
}

totalScorePart1 = 0
totalScorePart2 = 0
document.querySelector('pre').innerHTML.split("\n").forEach(function(singleRound) {
    if (singleRound == '') { return }
    totalScorePart1 = totalScorePart1 + answerTablePart1[singleRound];
    totalScorePart2 = totalScorePart2 + answerTablePart2[singleRound];
});
console.log(`Part 1: ${totalScorePart1}`);
console.log(`Part 2: ${totalScorePart2}`);