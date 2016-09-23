# Spot the difference game

Simple 'spot the difference' game developed for [BBC micro:bit](https://www.microbit.co.uk/)
in [MicroPython](https://micropython.org/).

## Gameplay

1. The game will show you basic instructions
2. Press left button (A) to start
3. Every round contains:
    1. Countdown before first image
    2. Randomly generated image
    3. Countdown between first and second image
    4. Second image which has different intensity in one pixel
    5. Question mark - this is your time to press left, right or no button
        * If the difference was in left two columns, press left button (A)
        * If the difference was in right two columns, press right button (B)
        * If the difference was in middle column, do not press any button
    6. The game will show you if you are right or not
4. At the end, you will see your score

## Levels

Levels depends on how many points you have. More points means harder game with more intensities of LED.

|  Points | Count of LED intensities | LED intensities |  
| ------- | ------------------------ | ----------------|  
|     < 5 |                        2 |          [0, 9] |  
|  <5, 9> |                        3 |       [0, 4, 9] |  
|    > 10 |                        4 |    [0, 3, 6, 9] |

## High score

My own highest score is 15 points.

## License

MIT
