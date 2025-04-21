
<template>
  <div class="chatbox">
    <input v-model="question" placeholder="请输入你的问题" />
    <button @click="ask">发送</button>
    <p v-if="answer">回答：{{ answer }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      question: '',
      answer: ''
    };
  },
  methods: {
    async ask() {
      const res = await axios.post('http://localhost:8000/ask', {
        question: this.question
      });
      this.answer = res.data.answer;
    }
  }
};
</script>

<style scoped>
.chatbox {
  padding: 20px;
}
</style>
