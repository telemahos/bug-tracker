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
                      Start Date
                    </CTableHeaderCell>
                    <CTableHeaderCell>Project</CTableHeaderCell>
                    <CTableHeaderCell class="text-center">
                      Due Date
                    </CTableHeaderCell>
                    <CTableHeaderCell class="text-center"
                      >Status</CTableHeaderCell
                    >
                    <CTableHeaderCell>Priority</CTableHeaderCell>
                    <CTableHeaderCell class="text-center"
                      >Action</CTableHeaderCell
                    >
                  </CTableRow>
                </CTableHead>
                <CTableBody>
                  <CTableRow
                    v-for="project in projects"
                    v-bind:value="project.id"
                    v-bind:key="project.due_date"
                  >
                    <CTableDataCell class="text-center">
                      <div>{{ project.start_date }}</div>
                    </CTableDataCell>
                    <CTableDataCell>
                      <div>
                        <CLink :href="link_to + project.id">{{
                          project.title
                        }}</CLink>
                      </div>
                      <div
                        class="small text-medium-emphasis text-truncate"
                        style="max-width: 250px"
                      >
                        {{ project.description }}
                      </div>
                    </CTableDataCell>
                    <CTableDataCell class="text-center">
                      <div>{{ project.due_date }}</div>
                    </CTableDataCell>
                    <CTableDataCell class="text-center">
                      <div class="small text-medium-emphasis">
                        <CBadge color="success">New</CBadge>
                      </div>
                    </CTableDataCell>
                    <CTableDataCell>
                      <div
                        class="small text-secondary"
                        color="text-secondary"
                        v-if="project.priority === 1"
                      >
                        Normal
                      </div>
                      <div
                        class="small text-info"
                        color="text-info"
                        v-if="project.priority === 2"
                      >
                        Medium
                      </div>
                      <div
                        class="small text-warning"
                        color="text-warning"
                        v-if="project.priority === 3"
                      >
                        High
                      </div>
                      <div
                        class="small text-danger"
                        color="text-danger"
                        v-if="project.priority === 4"
                      >
                        Critical
                      </div>
                    </CTableDataCell>
                    <CTableDataCell class="text-center">
                      <div>
                        <!-- <AppOffcanvasTicketEdit v-bind:the_case="project" /> -->
                        <CButton color="dark" variant="ghost" size="sm"
                          >Edit</CButton
                        >
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
import axios from 'axios'
// import AppOffcanvasTicketEdit from '../../components/AppOffcanvasTicketEdit.vue'

export default {
  name: 'ProjectList',
  components: {},
  data() {
    return {
      token: this.$store.state.token,
      apiURL: this.$store.state.apiURL,
      link_to: '#/theme/projectdetails/',
      today: '',
      start_date: '',
      due_date: '',
      title: '',
      description: '',
      ticketStatus: '',
      ticketPriority: '',
      projects: [],
      users: [],
    }
  },
  mounted() {
    const headers = {
      Authorization: `Bearer ${this.token}`,
      'Content-Type': 'application/json',
    }
    axios
      .get(`${this.apiURL}/project`, { headers })
      .then((response) => {
        this.projects = response.data
        // console.log('projects: ', this.projects)
      })
      .catch((error) => console.log(`${error}`))
    axios
      .get(`${this.apiURL}/user`, { headers })
      .then((response) => {
        this.users = response.data
        // console.log('User Names: ', this.users)
      })
      .catch((error) => console.log(`${error}`))
  },
}
</script>
