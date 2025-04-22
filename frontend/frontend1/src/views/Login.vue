<template>
  <div>
    <h2>Login</h2>
    <input v-model="username" placeholder="Username" />
    <input v-model="password" type="password" placeholder="Password" />
    <button @click="login">Login</button>
    <p>{{ message }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      message: ''
    };
  },
  methods: {
    async login() {
      try {
        const res = await axios.post('https://didactic-tribble-97j65vjp676wh975x-8000.app.github.dev/login', {
          username: this.username,
          password: this.password
        });
        this.message = res.data.message;
        this.$router.push('/hub');  // Redirect
      } catch (err) {
        this.message = 'Login failed!';
      }
    }
  }
};
</script>
