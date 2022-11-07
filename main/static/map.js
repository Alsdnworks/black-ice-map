const attribution =
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors';
const map = L.map("map");
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: attribution,
}).addTo(map);
map.fitWorld();

const markers = JSON.parse(document.getElementById("markers-data").textContent);

let feature = L.geoJSON(markers,{
    onEachFeature: function (feature, layer) {
            if (feature.properties.statLV ==1) {
            layer.setStyle({fillColor: '#0000FF ', fillOpacity: 0.5, color: '#0000FF ', weight: 0.1, opacity: 0.5});
            }
            else if (feature.properties.statLV ==2) {
            layer.setStyle({fillColor: '#FFFF00 ', fillOpacity: 0.5, color: '#FFFF00 ', weight: 0.1, opacity: 0.5});
            }
            else if (feature.properties.statLV ==3) {
            layer.setStyle({fillColor: '#FF0000 ', fillOpacity: 0.5, color: '#FF0000 ', weight: 0.1, opacity: 0.5});
            }
        }
    }).addTo(map);

map.fitBounds(feature.getBounds(), { padding: [100, 100] });
