from microbit import *
from random import choice

question_mark_image = Image("09900:"
                            "90090:"
                            "00900:"
                            "00000:"
                            "00900")


def count_down():
    """Count down from 3 to 1 with delay"""
    for x in reversed(range(1, 4)):
        display.clear()
        display.show(str(x))
        sleep(500)


def random_image(intensities):
    """Generate random image with random choice from intensities"""
    image = Image("00000:00000:00000:00000:00000:")
    for x in range(0, 4):
        for y in range(0, 4):
            image.set_pixel(x, y, choice(intensities))
    return image


def modify_image(image, intensities):
    """change one pixel to different intensity and show"""
    # Select random pixel on image
    x = choice(range(0, 4))
    y = choice(range(0, 4))

    # Get pixel intensity and remove it from array od new possible intensities
    pixel = image.get_pixel(x, y)
    possible_intensities = intensities.copy()
    possible_intensities.remove(pixel)

    # image modification
    image.set_pixel(x, y, choice(possible_intensities))

    # which answer is right for this image? Depends on column index
    if x in [0, 1]:
        right_answer = 'left'
    elif x in [3, 4]:
        right_answer = 'right'
    else:
        right_answer = 'middle'

    return image, right_answer


def wait_for_reply(miliseconds):
    """Show question mark and return count of button presses"""
    # clear display
    display.clear()
    # just for reset counters
    button_a.get_presses(), button_b.get_presses()
    # display question mark and wait
    display.show(question_mark_image)
    sleep(miliseconds)
    # return buttons stats
    return button_a.get_presses(), button_b.get_presses()


def main():
    """Main program"""
    # Initial intensities
    intensities = [0, 9]
    # How long show image
    show_image_time = 1500
    # How long show question mark and wait for reply
    question_delay = 2000
    # Initial score
    score = 0

    # Reset buttons state/counters
    button_a.was_pressed()
    button_b.was_pressed()

    display.scroll("Find difference between two images and press left, right or no button", delay=100)
    sleep(200)
    display.scroll("Press left button to start", delay=100)
    display.show(Image.ARROW_W)

    while not button_a.was_pressed():
        sleep(10)

    while True:
        count_down()
        # prepare random image
        image = random_image(intensities)
        # show it to player
        display.show(image)
        sleep(show_image_time)
        # break between images
        count_down()
        # generate modified image and right ansfer
        modified_image, right_answer = modify_image(image, intensities)
        # show modified image and wait
        display.show(modified_image)
        sleep(show_image_time)
        # get button statuses
        a, b = wait_for_reply(question_delay)

        if a == b:
            answer = 'middle'
        if a > b:
            answer = 'left'
        if b > a:
            answer = 'right'

        if answer == right_answer:
            # Good answer
            display.show(Image.YES)
            # increase score and make game harder
            score += 1
            if score < 5:
                intensities = [0, 9]
            elif score >= 5 and score < 10:
                intensities = [0, 4, 9]
            elif score >= 10:
                intensities = [0, 3, 6, 9]
            sleep(2000)
        else:
            # Bad answer
            display.show(Image.NO)
            sleep(2000)
            break

    display.scroll("Game over! Score: {}".format(score), delay=100, loop=True)


if __name__ == '__main__':
    main()
