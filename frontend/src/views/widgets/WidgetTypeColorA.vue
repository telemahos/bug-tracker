<template>
  <CRow>
    <CCol>
      <CCard class="mb-4">
        <CCardHeader>
          <strong>Vue Widgets</strong>
        </CCardHeader>
        <CCardBody>
          <h1>TEST</h1>
          <CRow>
            <CCol :sm="6" :lg="3">
              <CWidgetStatsB
                class="mb-4"
                color="success"
                inverse
                :progress="{ value: 100 }"
                text="Widget helper text"
                title="Active Projects"
                value="2 Projects"
              />
            </CCol>
            <CCol :sm="6" :lg="3">
              <CWidgetStatsB
                class="mb-4"
                color="info"
                inverse
                :progress="{ value: 50 }"
                text="Widget helper text"
                title="Total Tickets"
                value="17"
              />
            </CCol>
            <CCol :sm="6" :lg="3">
              <CWidgetStatsB
                class="mb-4"
                color="warning"
                inverse
                :progress="{ value: 75 }"
                text="Widget helper text"
                title="Unassigned Tickets"
                value="6"
              />
            </CCol>
            <CCol :sm="6" :lg="3">
              <CWidgetStatsB
                class="mb-4"
                color="primary"
                inverse
                :progress="{ value: 75 }"
                text="Widget helper text"
                title="Analytics"
                value="23"
              />
            </CCol>
          </CRow>

          <CRow>
            <WidgetCardA :id="grp1" />
            <WidgetCardA :id="grp2" />
            <WidgetCardA :id="grp3" />
            <WidgetCardA :id="grp4" />
          </CRow>
        </CCardBody>
      </CCard>
    </CCol>
  </CRow>
</template>

<script>
import WidgetCardA from '../widgets/WidgetCardA.vue'

export default {
  name: 'WidgetTypeColorA',
  components: {
    WidgetCardA,
  },
}
</script>
