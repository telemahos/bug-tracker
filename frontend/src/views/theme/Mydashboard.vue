<template>
  <div>
    <h1>Hallo Mydashboard!</h1>
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
}
</script>
