import sys
from geocoder import get_coordinates, get_ll_span

from mapapi_PG import show_map


def main():
    toponym = ' '.join(sys.argv[1:])

    if toponym:
        lat, lon = get_coordinates(toponym)
        ll_spn = f'll={lat},{lon}&spn=0.005,0.005'
        show_map(ll_spn, "map")

        # ll, spn = get_ll_span(toponym)
        # ll_spn = f'll={ll},{lon}&spn={spn}'
        # point_param = f'pt={ll}'
        # show_map(ll_spn, "map", add_params=point_param)
    else:
        print('No data')

if __name__ == '__main__':
    main()
