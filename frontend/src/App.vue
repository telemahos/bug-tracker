<template>
  <div id="proto">
    <router-view />
    <!-- <router-view route="Login"/> -->
    <!-- <Login />  -->
  </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios'
import Login from '@/views/pages/Login'
export default {
  beforeCreate() {
    this.$store.commit('initializeApp')
    const token = this.$store.state.token
    if (token) {
      axios.defaults.headers.common['Authorization'] = 'Token ' + token
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
}
/* eslint-enable */
</script>

<style lang="scss">
// Import Main styles for this application
@import 'styles/style';
</style>
