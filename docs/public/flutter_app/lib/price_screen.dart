import 'package:flutter/material.dart';

class PriceScreen extends StatelessWidget {
  final Map<String, double> prices = {
    'USA': 300,
    'Japan': 30,
    'India': 10,
  };

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Drug Price Comparison')),
      body: ListView(
        children: prices.entries.map((entry) {
          return ListTile(
            title: Text(entry.key),
            trailing: Text('\$${entry.value.toStringAsFixed(2)}'),
          );
        }).toList(),
      ),
    );
  }
}


