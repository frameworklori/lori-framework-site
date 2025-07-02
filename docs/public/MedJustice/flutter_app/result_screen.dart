
import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:flutter/services.dart';

class ResultScreen extends StatefulWidget {
  @override
  _ResultScreenState createState() => _ResultScreenState();
}

class _ResultScreenState extends State<ResultScreen> {
  List<dynamic> predictions = [];

  @override
  void initState() {
    super.initState();
    loadPredictions();
  }

  Future<void> loadPredictions() async {
    final String jsonStr = await rootBundle.loadString('assets/predicted_costs.json');
    final List<dynamic> data = json.decode(jsonStr);
    setState(() {
      predictions = data;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Predicted Costs')),
      body: ListView.builder(
        itemCount: predictions.length,
        itemBuilder: (context, index) {
          final item = predictions[index];
          return ListTile(
            title: Text('${item['ethnicity']} - ${item['category']}'),
            subtitle: Text('\$${(item['predicted_costs'] / 1000000).toStringAsFixed(1)}M'),
          );
        },
      ),
    );
  }
}
