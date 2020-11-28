var map = new ol.Map({
    target: 'map',
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM()
      })
    ],
    view: new ol.View({
      center: ol.proj.fromLonLat([ 121.05041, 14.65306 ]),
      zoom: 15
    })
  });

  https://www.mapquestapi.com/geocoding/v1/reverse?key=GZiAVJKnwv1sRwkrbXrKvKZwi3xMEs32&location=14.65859%2C121.04962&outFormat=json&thumbMaps=false


