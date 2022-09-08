<template>
  <div>
    <CRow>
      <CCol :md="12">
        <h2>Projects</h2>
        <CLink href="#/theme/projectnew"
          ><h5><CBadge color="info">New Project +</CBadge></h5></CLink
        >
        <br /><br /><br />
      </CCol>
    </CRow>
  </div>
  <div>
    <CRow>
      <CCol :md="12">
        <CCard class="mb-4">
          <CCardBody>
            <CRow>
              <CCol :sm="5">
                <h4 id="traffic" class="card-title mb-0">Projects</h4>
                <div class="small text-medium-emphasis">September 2022</div>
              </CCol>
              <CTable align="middle" class="mb-0 border" hover responsive>
                <CTableHead color="light">
                  <CTableRow>
                    <CTableHeaderCell class="text-center">
                      <!--<CIcon name="cil-people" />-->Due Date
                    </CTableHeaderCell>
                    <CTableHeaderCell>Title</CTableHeaderCell>
                    <CTableHeaderCell class="text-center"
                      >Status</CTableHeaderCell
                    >
                    <CTableHeaderCell>Priority</CTableHeaderCell>
                    <CTableHeaderCell class="text-center"
                      >Type</CTableHeaderCell
                    >
                    <CTableHeaderCell>Project</CTableHeaderCell>
                    <CTableHeaderCell class="text-center"
                      >Owner</CTableHeaderCell
                    >
                    <CTableHeaderCell class="text-center"
                      >ToDo</CTableHeaderCell
                    >
                  </CTableRow>
                </CTableHead>
                <CTableBody>
                  <CTableRow
                    v-for="(the_case, index) in cases"
                    v-bind:value="the_case.id"
                    v-bind:key="the_case.due_date"
                  >
                    <CTableDataCell class="text-center">
                      <div>{{ the_case.due_date }}</div>
                      <!-- <CAvatar
                       :key="case.name"
                        size="md"
                        :src="item.avatar.src"
                        :status="item.avatar.status"
                      /> -->
                    </CTableDataCell>
                    <CTableDataCell>
                      <div>
                        <a href="#" target="_blank" rel="noopener noreferrer">{{
                          the_case.title
                        }}</a>
                      </div>
                      <div
                        class="small text-medium-emphasis text-truncate"
                        style="max-width: 150px"
                      >
                        {{ the_case.description }}
                      </div>
                    </CTableDataCell>
                    <CTableDataCell class="text-center">
                      <div
                        class="small text-medium-emphasis"
                        v-if="the_case.status === 1"
                      >
                        <CBadge color="success">New</CBadge>
                      </div>
                      <div
                        class="small text-medium-emphasis"
                        v-if="the_case.status === 2"
                      >
                        <CBadge color="info">In Progress</CBadge>
                      </div>
                      <div
                        class="small text-medium-emphasis"
                        v-if="the_case.status === 3"
                      >
                        <CBadge color="warning">On Hold</CBadge>
                      </div>
                      <div
                        class="small text-medium-emphasis"
                        v-if="the_case.status === 4"
                      >
                        <CBadge color="dark">Solved</CBadge>
                      </div>
                      <!-- <CIcon
                        size="xl"
                        :name="item.country.flag"
                        :title="item.country.name"
                      /> -->
                    </CTableDataCell>
                    <CTableDataCell>
                      <div
                        class="small text-secondary"
                        color="text-secondary"
                        v-if="the_case.priority === 1"
                      >
                        Normal
                      </div>
                      <div
                        class="small text-info"
                        color="text-info"
                        v-if="the_case.priority === 2"
                      >
                        Medium
                      </div>
                      <div
                        class="small text-warning"
                        color="text-warning"
                        v-if="the_case.priority === 3"
                      >
                        High
                      </div>
                      <div
                        class="small text-danger"
                        color="text-danger"
                        v-if="the_case.priority === 4"
                      >
                        Critical
                      </div>
                      <!-- <div class="clearfix">
                        <div class="float-start">
                          <strong>{{ item.usage.value }}%</strong>
                        </div>
                        <div class="float-end">
                          <small class="text-medium-emphasis">
                            {{ item.usage.period }}
                          </small>
                        </div>
                      </div>
                      <CProgress
                        thin
                        :color="item.usage.color"
                        :value="item.usage.value"
                      /> -->
                    </CTableDataCell>
                    <CTableDataCell class="text-center">
                      <div
                        class="text-dark small"
                        v-if="the_case.case_type === 1"
                      >
                        Issue
                      </div>
                      <div
                        class="text-danger small"
                        v-if="the_case.case_type === 2"
                      >
                        Bug
                      </div>
                      <div
                        class="text-warning small"
                        v-if="the_case.case_type === 3"
                      >
                        Note
                      </div>
                      <!-- <CIcon size="xl" :name="item.payment.icon" /> -->
                    </CTableDataCell>
                    <CTableDataCell>
                      <div>{{ projectTitle[index] }}</div>
                      <!-- <div class="small text-medium-emphasis">Last login</div>
                      <strong>{{ item.activity }}</strong> {{ projectNames.title }}-->
                    </CTableDataCell>
                    <CTableDataCell class="text-center">
                      <div>{{ userNames[index] }}</div>
                      <!-- <CIcon size="xl" :name="item.payment.icon" /> -->
                    </CTableDataCell>
                    <CTableDataCell class="text-center">
                      <div>
                        <AppOffcanvasTicketEdit v-bind:the_case="the_case" />
                      </div>
                    </CTableDataCell>
                  </CTableRow>
                  <CTableRow> </CTableRow>
                </CTableBody>
              </CTable>
            </CRow>
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
  </div>
</template>

<script>
// import provide from 'vue'
// import axios from 'axios'
// import AppOffcanvasTicketEdit from '../../components/AppOffcanvasTicketEdit.vue'

export default {
  name: 'ProjectList',
  components: {},
  data() {
    return {}
  },
  mounted() {},
}
</script>
