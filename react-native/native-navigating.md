# 리액트 네이티브 화면 이동

### 📑Navigating Between Screens

`android studio` 의 `indent`를 `react native` 모듈로 구현 가능하다.

✔️다운로드
```node.js
// install
npm install @react-navigation/native @react-navigation/native-stack
npm install react-native-screens react-native-safe-area-context
```  

```js
return(
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen
          name="Home"
          component={MainPage}
          //header 부분 삭제
          options={{ headerShown: false }}
        />
        <Stack.Screen 
          name="CapturePhoto" 
          component={CapturePhoto} 
          options={{ headerShown: false }}
        />
        <Stack.Screen 
          name="UploadPhoto" 
          component={UploadPhoto} 
          options={{ headerShown: false }}
        />
      </Stack.Navigator>
    </NavigationContainer>
```
app.js 에서 이렇게 선언하고 `component`에서는

```js
const CapturePhoto = ({navigation}) => {
//이렇게 매개변수 부분에 `navigation`을 넣고
//후에 결과창으로 리다이렉트를 할려면
   navigation.navigate('resultpage');
//함수 안에서 이렇게 다른 페이지로 이동하면 된다
```

다른 컴포넌트로 `props`를 주고 싶을때가 있다
그럴때는

```js
<Button
      title="Go to Jane's profile"
      onPress={() =>
        navigation.navigate('Profile', { name: 'Jane' })
      }
// navigation.navigate 뒤에 { name: 'Jane' } 을 주고
const ProfileScreen = ({ navigation, route }) => {
  return <Text>This is {route.params.name}'s profile</Text>;
};
// ProfileScreen 에서 route.params.~~를 이용해 받을 수 있다.
```
<a href="https://reactnative.dev/docs/navigation">참고한 웹사이트</a>
