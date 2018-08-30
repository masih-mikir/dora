from math import sqrt

recreations = [
    {
        "recreation_id": 1,
        "recreation_name": "Taman Impian Jaya Ancol",
        "recreation_time_minute": 120,
        "recreation_price": 200000,
        "position_lat": -6.126219,
        "position_long": 106.831017,
        "recreation_image": "http://cdn2.tstatic.net/kaltim/foto/bank/images/pantai-lagoon-ancol_20180620_055758.jpg",
        "recreation_city": "bandung",
        "recreation_description": "Taman Impian Jaya Ancol merupakan sebuah objek wisata di bumi sari natar Jakarta Utara. Sebagai komunitas pembaharuan kehidupan masyarakat yang menjadi kebanggaan bangsa. Senantiasa menciptakan lingkungan sosial yang lebih baik melalui sajian hiburan berkualitas yang berunsur seni, budaya dan pengetahuan, dalam rangka mewujudkan komunitas 'Life Re-Creation' yang menjadi kebanggaan bangsa."
    },
    {
        "recreation_id": 2,
        "recreation_name": "Monumen Nasional",
        "recreation_time_minute": 120,
        "recreation_price": 200000,
        "position_lat": -6.175392,
        "position_long": 106.827153,
        "recreation_image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Merdeka_Square_Monas_02.jpg/240px-Merdeka_Square_Monas_02.jpg",
        "recreation_city": "bandung",
        "recreation_description": "Monumen Nasional atau yang populer disingkat dengan Monas atau Tugu Monas adalah monumen peringatan setinggi 132 meter (433 kaki) yang didirikan untuk mengenang perlawanan dan perjuangan rakyat Indonesia untuk merebut kemerdekaan dari pemerintahan kolonial Hindia Belanda. Pembangunan monumen ini dimulai pada tanggal 17 Agustus 1961 di bawah perintah presiden Sukarno, dan dibuka untuk umum pada tanggal 12 Juli 1975. Tugu ini dimahkotai lidah api yang dilapisi lembaran emas yang melambangkan semangat perjuangan yang menyala-nyala. Monumen Nasional terletak tepat di tengah Lapangan Medan Merdeka, Jakarta Pusat. Monumen dan museum ini dibuka setiap hari mulai pukul 08.00 - 15.00 WIB. Pada hari Senin pekan terakhir setiap bulannya ditutup untuk umum."
    },
    {
        "recreation_id": 3,
        "recreation_name": "Kota Tua",
        "recreation_time_minute": 120,
        "recreation_price": 200000,
        "position_lat": -6.134662,
        "position_long": 106.813371,
        "recreation_image": "https://www.pikniek.com/wp-content/uploads/2017/10/000024-00_wisata-kota-tua-jakarta_kota-tua_800x450_ccpdm-min.jpg",
        "recreation_city": "bandung",
        "recreation_description": "Kota Tua Jakarta, juga dikenal dengan sebutan Batavia Lama (Oud Batavia), adalah sebuah wilayah kecil di Jakarta, Indonesia. Wilayah khusus ini memiliki luas 1,3 kilometer persegi melintasi Jakarta Utara dan Jakarta Barat (Pinangsia, Taman Sari dan Roa Malaka). Dijuluki 'Permata Asia' dan 'Ratu dari Timur' pada abad ke-16 oleh pelayar Eropa, Jakarta Lama dianggap sebagai pusat perdagangan untuk benua Asia karena lokasinya yang strategis dan sumber daya melimpah"
    }
]


def euclidian_distance(origin_latitude, origin_longitude, destination_latitude, destination_longitude):
    distance = sqrt((origin_latitude - destination_latitude) ** 2 + (origin_longitude - destination_longitude) ** 2)
    return distance


def get_itinerary(recreations, origin_latitude, origin_longitude, start_time, end_time):
    """
    Using brute force algorithm to decide the route.
    :type recreations: list
    :return: array of places
    """

    max_trip_minute = get_max_trip_minute(start_time, end_time)

    recreation_trip = []
    trip_minute = 0
    while trip_minute <= max_trip_minute and len(recreations) > 0:
        distances = []
        for recreation in recreations:
            distances.append(euclidian_distance(origin_latitude, origin_longitude, recreation['position_lat'],
                                                recreation['position_long']))
        print(distances)
        recreation_trip.append(recreations.pop(distances.index(min(distances))))
        origin_latitude = recreation_trip[-1]['position_lat']
        origin_longitude = recreation_trip[-1]['position_long']
    return recreation_trip


def get_max_trip_minute(start_time, end_time):
    return (end_time - start_time) * 60
