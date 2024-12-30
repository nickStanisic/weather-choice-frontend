function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
      center: { lat: 39.0, lng: -105.5 },
      zoom: 7,
    });

    if (window.pointsData && window.pointsData.length) {
        window.pointsData.forEach(pt => {
          const iconUrl = pt.valid
            ? "http://maps.google.com/mapfiles/ms/icons/green-dot.png"
            : "http://maps.google.com/mapfiles/ms/icons/red-dot.png";
    
          new google.maps.Marker({
            position: { lat: pt.lat, lng: pt.lon },
            map: map,
            title: `Temp: ${pt.temp}`,
            icon: iconUrl
          });
        });
      }
  }