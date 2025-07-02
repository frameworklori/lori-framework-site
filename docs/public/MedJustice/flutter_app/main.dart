import 'package:flutter/material.dart';
import 'price_screen.dart';
import 'result_screen.dart';

void main() {
  runApp(MedJusticeApp());
}

class MedJusticeApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'MedJustice',
      theme: ThemeData(primarySwatch: Colors.teal),
      home: HomePage(),
    );
  }
}

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('MedJustice Home')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              child: Text('📊 Compare Drug Prices'),
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => PriceScreen()),
                );
              },
            ),
            ElevatedButton(
              child: Text('📈 View Cost Predictions'),
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => ResultScreen()),
                );
              },
            ),
          ],
        ),
      ),
    );
  }
}

