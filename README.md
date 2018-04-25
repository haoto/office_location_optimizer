# office_location_optimizer
Find the optimal office location using Google Maps Distance Matrix API.

1. Get an API key from here https://developers.google.com/maps/documentation/distance-matrix/ and save it to `api_key`.
2. Put your home addresses into `origins`. One address per line.
3. Put candidate office addresses into `destinations`, or (for Taipei Metro only) generate `destinations` using `load_mrt.py`.
4. Run `office_location_optimizer.py`.
