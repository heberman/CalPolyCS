from quakeFuncs import *

def main():
    f = 'quakes.txt'
    quakes = read_quakes_from_file(f)
    display_quakes(quakes)
    while 2 + 2 == 4:
        display_options()
        choice = input("\nChoice: ")
        if choice == 's':
            sort_choice = input("Sort by (m)agnitude, (t)ime, (l)ongitude, or l(a)titude? ").lower()
            if sort_choice == 'm':
                quakes = sorted(quakes, key=lambda x: x.mag, reverse=True)
                display_quakes(quakes)
            elif sort_choice == 't':
                quakes = sorted(quakes, key=lambda x: x.time, reverse=True)
                display_quakes(quakes)
            elif sort_choice == 'l':
                quakes = sorted(quakes, key=lambda x: x.longitude)
                display_quakes(quakes)
            elif sort_choice == 'a':
                quakes = sorted(quakes, key=lambda x: x.latitude)
                display_quakes(quakes)
        elif choice == 'f':
            filter_choice = input("Filter by (m)agnitude or (p)lace? ").lower()
            if filter_choice == 'm':
                lower_bound = float(input("Lower bound: "))
                upper_bound = float(input("Upper bound: "))
                new_quakes = filter_by_mag(quakes, lower_bound, upper_bound)
                display_quakes(new_quakes)
            elif filter_choice == 'p':
                keyword = input("Search for what string? ")
                new_quakes = filter_by_place(quakes, keyword)
                display_quakes(new_quakes)
        elif choice == 'n':
            x = get_json('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson')
            for item in x:
                features = x["features"]
            isQuakes = False
            for event in features:
                quake = quake_from_feature(event)
                if quake not in quakes:
                    quakes.append(quake)
                    isQuakes = True
            if isQuakes:
                print("\nNew quakes found!!!")
            display_quakes(quakes)
        elif choice == 'q':
            write_data(quakes)
            quit()

if __name__ == '__main__':
    main()