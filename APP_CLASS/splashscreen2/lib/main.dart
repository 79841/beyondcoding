import 'package:flutter/material.dart';
import 'package:splashscreen2/screen/splash_screen.dart';

void main() {
  runApp(
    MaterialApp(
      theme: ThemeData(
        fontFamily: 'NotoSans',
      ),
      home: const SplashScreen(),
    ),
  );
}
