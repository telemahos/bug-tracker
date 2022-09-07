<template>
  <div>
    <CRow>
      <CCol :md="12">
        <h2>Tickets in Projects</h2>
        <CLink href="#/theme/ticketnew"
          ><h5><CBadge color="info">New Ticket +</CBadge></h5></CLink
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
                <h4 id="traffic" class="card-title mb-0">Tickets</h4>
                <div class="small text-medium-emphasis">August 2022</div>
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
                      <div class="small text-medium-emphasis text-truncate" style="max-width: 150px;">
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
import axios from 'axios'
import AppOffcanvasTicketEdit from '../../components/AppOffcanvasTicketEdit.vue'

export default {
  name: 'Ticket',
  components: {
    AppOffcanvasTicketEdit,
  },
  data() {
    return {
      token: this.$store.state.token,
      apiURL: this.$store.state.apiURL,
      cases: [],
      date: '',
      title: '',
      description: '',
      ticketStatus: '',
      ticketPriority: '',
      ticketType: '',
      projects: [],
      users: [],
      userNames: [],
      projectTitle: [],
      all_cases: [],
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
        this.$store.commit('setProjects', this.projects)
        // console.log('projects: ', this.projects)
      })
      .catch((error) => console.log(`${error}`))
    axios
      .get(`${this.apiURL}/user`, { headers })
      .then((response) => {
        this.users = response.data
        this.$store.commit('setUsers', this.users)
        // console.log('User Names: ', this.users)
      })
      .catch((error) => console.log(`${error}`))
    axios
      .get(`${this.apiURL}/case`, { headers })
      .then((response) => {
        this.cases = response.data
        console.log('Cases: ', this.cases)
      })
      .finally(() => {
        let y = 0,
          z = 0
        for (let i = 0; i < this.cases.length; i++) {
          // Find the project title of each case
          for (let e = 0; e < this.projects.length; e++) {
            if (this.cases[i].project_id === this.projects[e].id) {
              this.projectTitle[y] = this.projects[e].title
              y++
            }
          }
          // Find the owners name of each case
          for (let f = 0; f < this.users.length; f++) {
            if (this.cases[i].owner_id === this.users[f].id) {
              this.userNames[z] = this.users[f].name
              z++
            }
          }
          // Find the status of each case
          // if (this.cases[i].status === 1) {
          //   this.ticketStatus[i] = "Issue";
          //   x++;
          // }
          // else if (this.cases[i].status === 2) {
          //   this.ticketStatus[x] = "Bug";
          //   x++;
          // }
          // else if (this.cases[i].status === 3) {
          //   this.ticketStatus[x] = "Note";
          //   x++;
          // }
        }
      })
      .catch((error) => console.log(`${error}`))
  },
  // provide: {
  //   all_cases: this.cases,
  // },
}
</script>
