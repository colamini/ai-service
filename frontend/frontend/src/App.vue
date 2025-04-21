
<template>
  <div id="app">
    <ChatBox />
  </div>
</template>

<script>
import ChatBox from './components/ChatBox.vue';

export default {
  name: 'App',
  components: {
    ChatBox
  }
};
</script>

<style>
#app {
  text-align: center;
}
</style>
