The keller-* lists come from:
https://solitairelaboratory.com/fclists.html

The fcgs-* lists come from:
https://freecellgamesolutions.com/stats.html

hard.txt and easy.txt combine the above sources. Each entry in easy.txt appears
three times, to oversample and be more proportional to easy.txt. (Er, but will
this lead to overfitting, since the same same easy deals will likely be in the
train and validation sets?)

Editorial notes:
- The original sources occasionally include some indication of how difficult
  a specific deal is; the dantes collection does not include that information.
- Deals marked as having short solutions are included under easy, and long
  solutions under hard.
- Impossible deals are included under hard.
