<template>
  <CCol :lg="3">
    <!-- <CCard> -->
    <CWidgetStatsF
      class="my-1"
      color="secondary"
      :padding="false"
      :title="grp1.field1"
      value="18"
    >
      <template #icon>
        <CIcon icon="cil-people" size="xl" />
      </template>
    </CWidgetStatsF>
    <CWidgetStatsF
      class="my-1"
      color="dark"
      :padding="false"
      :title="grp1.field3"
      value="10"
    >
      <template #icon>
        <CIcon icon="cil-chart-pie" size="xl" />
      </template>
    </CWidgetStatsF>
    <CWidgetStatsF
      class="my-1"
      color="info"
      :padding="false"
      :title="grp1.field2"
      value="36"
    >
      <template #icon>
        <CIcon icon="cil-check" size="xl" />
      </template>
    </CWidgetStatsF>
    <!-- </CCard> -->
  </CCol>
</template>

<script>
export default {
  data() {
    return {
      grp1: {
        field1: 'Total Users',
        field2: 'Tickets in Progress',
        field3: 'Total Developers',
      },
      grp2: {
        field1: 'test11',
        field2: 'test22',
        field3: 'test33',
      },
      grp3: {
        field1: 'test111',
        field2: 'test222',
        field3: 'test333',
      },
    }
  },
}
</script>
