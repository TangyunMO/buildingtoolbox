from buildingtoolbox.query_weather import search_city,main



def test_main():
    assert len(main('london')) != 0
