import 'package:flutter/material.dart';
import 'package:flutter_osm_plugin/flutter_osm_plugin.dart';
import 'package:geo_quest_app/splash.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const Splash(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {

  bool markerAdded = false;
  List<GeoPoint> markerPoints = [];

  final _mapController = MapController.withUserPosition(
        trackUserLocation: const UserTrackingOption(
           enableTracking: true,
           unFollowUser: false,
        )
  );

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addPostFrameCallback((timeStamp) {
      _mapController.listenerMapLongTapping.addListener(() async{

        if (markerPoints.isNotEmpty) {
          await _mapController.removeMarker(markerPoints[0]);
          await _mapController.clearAllRoads();
          markerPoints.removeAt(0);
          markerAdded = false;
        }

        GeoPoint userLocation = await _mapController.myLocation();
        var position = _mapController.listenerMapLongTapping.value;

        if (position != null) {
          markerPoints.add(position);
          await _mapController.addMarker(position, markerIcon: const MarkerIcon(
              icon: Icon(Icons.pin_drop, color: Colors.black,),
          ));

          
           RoadInfo roadInfo = await _mapController.drawRoad( 
            userLocation,
            GeoPoint(latitude: position.latitude, longitude: position.longitude),
            roadType: RoadType.car,
            roadOption: const RoadOption(
                roadWidth: 10,
                roadColor: Colors.blue,
                zoomInto: false,
            ),
          );
          markerAdded = true;
        }

        setState(() {});
      });
    });
  }
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.green,
        
        title:  const Center(
          child: Text('GeoQuest', style: TextStyle(color: Colors.white,)),
          )
        ),
      body: OSMFlutter( 
        controller:_mapController,
        osmOption: OSMOption(
              userTrackingOption: const UserTrackingOption(
              enableTracking: true,
              unFollowUser: false,
            ),
            zoomOption: const ZoomOption(
                  initZoom: 8,
                  minZoomLevel: 3,
                  maxZoomLevel: 19,
                  stepZoom: 1.0,
            ),
            userLocationMarker: UserLocationMaker(
                personMarker: const MarkerIcon(
                    icon: Icon(
                        Icons.location_history_rounded,
                        color: Colors.red,
                        size: 48,
                    ),
                ),
                directionArrowMarker: const MarkerIcon(
                    icon: Icon(
                        Icons.double_arrow,
                        size: 48,
                    ),
                ),
            ),
            roadConfiguration: const RoadOption(
                    roadColor: Colors.yellowAccent,
            ),
            markerOption: MarkerOption(
                defaultMarker: const MarkerIcon(
                    icon: Icon(
                      Icons.person_pin_circle,
                      color: Colors.blue,
                      size: 56,
                    ),
                )
            ),
        ),
        onMapIsReady: (isReady) async {
          if(isReady) {
            await Future.delayed(const Duration(seconds: 1), () async {
              await _mapController.currentLocation();
            }
           );
          }
        },
    ),
      bottomNavigationBar: BottomAppBar(
        color: Colors.green,
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Center(child: Text(
              markerAdded
                  ? 'Time: XX min        Distance: XX km' 
                  : 'Long Tap to place a marker!',
               style: const TextStyle(
                color: Colors.white,
                fontSize: 20,
              ),
            ),
          ),
        )
      ),
    );
  }
}

