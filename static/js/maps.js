function createSquare(map, centerLat, centerLng, delta, color) {
  // delta is the side length of the square in degrees
  // e.g., 0.02 ≈ 2 km x 2 km near the equator (less near higher latitudes)
  const halfDelta = delta / 2;
  const bounds = {
    north: centerLat + halfDelta,
    south: centerLat - halfDelta,
    east: centerLng + halfDelta,
    west: centerLng - halfDelta
  };

  return new google.maps.Rectangle({
    strokeColor: color,
    strokeOpacity: 0.25,
    strokeWeight: 2,
    fillColor: color,
    fillOpacity: 0.25, 
    map: map,
    bounds: bounds
  });
}

function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
      center: { lat: 39.0, lng: -105.5 },
      zoom: 7
    });

    if (window.pointsData && window.pointsData.length) {
        window.pointsData.forEach(pt => {
          const color = pt.valid
            ? 'green'
            : 'red';

          createSquare(map, pt.lat, pt.lon, 0.125, color);

        });
      }
  }