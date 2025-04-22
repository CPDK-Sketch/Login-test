<template>
  <div id="app">
    <!-- Navigation Bar -->
    <nav v-if="isLoggedIn">
      <ul>
        <li><router-link to="/">Login</router-link></li>
        <li><router-link to="/returns">Returns</router-link></li>
        <li><router-link to="/admin">Admin</router-link></li>
        <li><router-link to="/billing">Billing</router-link></li>
        <li><router-link to="/hub">Hub</router-link></li>
      </ul>
    </nav>

    <!-- Dynamic Content -->
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      isLoggedIn: false,  // Add a state to check if user is logged in
    };
  },
  watch: {
    $route(to, from) {
      if (to.name === 'Login' && this.isLoggedIn) {
        this.isLoggedIn = false;  // Reset login state if already logged in
      }
    }
  }
};
</script>

<style scoped>
/* Global Styles */
#app {
  font-family: Arial, sans-serif;
  background-color: #f4f4f9;
  min-height: 100vh;
}

nav {
  background-color: #333;
  padding: 10px;
  text-align: center;
}

nav ul {
  list-style: none;
  padding: 0;
}

nav li {
  display: inline;
  margin: 0 15px;
}

nav a {
  color: white;
  text-decoration: none;
  font-size: 18px;
}

nav a:hover {
  color: #ff5722;
}
</style>
