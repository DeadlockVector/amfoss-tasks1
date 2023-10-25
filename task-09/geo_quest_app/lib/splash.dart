import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:flutter/material.dart';
import 'package:geo_quest_app/main.dart';


class Splash extends StatefulWidget {
  const Splash({super.key});

  @override
  State<Splash> createState() => _SplashState();
}

class _SplashState extends State<Splash> {

  @override
  void initState() {
    super.initState();
    _navigateToHome();
  }

  _navigateToHome() async {
    await Future.delayed(Duration(milliseconds: 3000), () {});
    Navigator.pushReplacement(
      context, 
      MaterialPageRoute(builder: (context) => const MyHomePage())
    );
  }

  @override
  Widget build(BuildContext context) {
    return const Scaffold(
      body: Center(
        child: SpinKitWaveSpinner(
          color: Colors.green,
          trackColor: Color.fromARGB(255, 1, 92, 39),
          waveColor: Color.fromARGB(255, 38, 163, 90),
          size: 200,
        )
      )
    );
  }
}