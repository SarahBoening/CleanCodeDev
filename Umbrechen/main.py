import Umbrechen.text_wrapper as tw


def main():
    text = "Es blaut die Nacht, die Sternlein blinken,\nSchneeflöcklein leis herniedersinken.\n" \
           "Auf Edeltännleins grünem Wipfel\nläuft sich ein kleiner weißer Zipfel.\n " \
           "Und dort vom Fenster her durchbricht\nden dunklen Tann ein warmes Licht."
    max_width = 9
    new_text = tw.wrap(text, max_width)
    print(new_text)


if __name__ == "__main__":
    main()
