// question: given an integer, number of heads and tails, return probability

function coinFlipProbability(step, h, t) {
    if (h < 0 || t < 0) {
        return 0;
    }
    if (step == 0) {
        return 1;
    }
    return coinFlipProbability(step - 1, h - 1, t) + coinFlipProbability(step - 1, h, t - 1);
}

console.log(coinFlipProbability(3, 2, 1))