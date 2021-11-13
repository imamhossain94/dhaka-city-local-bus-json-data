# dhaka-city-local-bus-json-data

JSON Data:
```json
{
  "data": [
    {
      "english": "Achim Paribahan",
      "bangle": "আছিম পরিবহন",
      "image": "https://firebasestorage.googleapis.com/v0/b/bd-bus-route-32221.appspot.com/o/buses%2F%E0%A6%86%E0%A6%9B%E0%A6%BF%E0%A6%AE%20%E0%A6%AA%E0%A6%B0%E0%A6%BF%E0%A6%AC%E0%A6%B9%E0%A6%A8.jpg?alt=media&token=796ceee2-da0e-4ae4-9ffd-74a0f6c7a6ee",
      "routes": [
        "Gabtoli", "Technical", "Ansar Camp", "Mirpur 1", "Sony Cinema Hall", "Mirpur 2", "Mirpur 10", "Mirpur 11", "Purobi", "Kalshi", "ECB Square", "MES", "Shewra", "Kuril Bishwa Road", "Jamuna Future Park", "Bashundhara", "Nadda", "Notun Bazar", "Bashtola","Shahjadpur", "Uttar Badda", "Badda – Madhya Badda", "Merul", "Rampura Bridge", "Banasree", "Demra Staff Quarter"
      ],
      "time": "",
      "service_type": "Semi-Sitting Service(Check System)"
    }
  ]
}
```



Dart Model: <a href="https://javiercbk.github.io/json_to_dart/">json_to_dart</a>
```dart
class BusData {
  List<Data> data;

  BusData({this.data});

  BusData.fromJson(Map<String, dynamic> json) {
    if (json['data'] != null) {
      data = new List<Data>();
      json['data'].forEach((v) {
        data.add(new Data.fromJson(v));
      });
    }
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    if (this.data != null) {
      data['data'] = this.data.map((v) => v.toJson()).toList();
    }
    return data;
  }
}

class Data {
  String english;
  String bangle;
  String image;
  List<String> routes;
  String time;
  String serviceType;

  Data({this.english, this.bangle, this.image, this.routes, this.time, this.serviceType});

  Data.fromJson(Map<String, dynamic> json) {
    english = json['english'];
    bangle = json['bangle'];
    image = json['image'];
    routes = json['routes'].cast<String>();
    time = json['time'];
    serviceType = json['service_type'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['english'] = this.english;
    data['bangle'] = this.bangle;
    data['image'] = this.image;
    data['routes'] = this.routes;
    data['time'] = this.time;
    data['service_type'] = this.serviceType;
    return data;
  }
}
```

Kotlin Data Model: <a href="https://www.json2kotlin.com/">json2kotlin</a>

```kotlin

implementation "com.google.code.gson:gson:2.8.8"

val json = getJson()
val topic = Gson().fromJson(json, BusData::class.java)

data class BusData (
	@SerializedName("data") val data : List<Data>
)

data class Data (
	@SerializedName("english") val english : String,
	@SerializedName("bangle") val bangle : String,
	@SerializedName("bangle") val image : String,
	@SerializedName("routes") val routes : List<String>,
	@SerializedName("time") val time : String,
	@SerializedName("service_type") val service_type : String
)
```
