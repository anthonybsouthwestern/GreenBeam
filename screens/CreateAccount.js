import { StyleSheet, Text, View } from 'react-native';

import React from 'react';

// let btn = document.createElement("button");
// btn.innerHTML = "Create A New Account";

export default function App() {
  return (
    <View style={styles.container}>
      <Text>Account</Text>
      <Text>document.body.appendChild(btn)</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});