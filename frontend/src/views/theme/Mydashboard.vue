<template>
  <div>
    <h1>My Dashboard</h1>
    <WidgetTypeColorA />
    <WidgetCardA />
    <WidgetsStatsA />
    <WidgetsStatsD />
  </div>
</template>

<script>
import WidgetsStatsA from '../widgets/WidgetsStatsTypeA.vue'
import WidgetsStatsD from '../widgets/WidgetsStatsTypeD.vue'
import WidgetTypeColorA from '../widgets/WidgetTypeColorA.vue'

export default {
  name: 'Mydashboard',
  components: {
    WidgetsStatsA,
    WidgetsStatsD,
    WidgetTypeColorA,
  },
  data() {
    return {
      // projectID: this.id,
      token: this.$store.state.token,
      apiURL: this.$store.state.apiURL,
    }
  },
  beforeMount() {
    // this.loadProject()
    // this.loadUsersAndProjects()
  },
  
}
</script>
