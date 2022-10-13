<template>
  <h1>Members List!</h1>

  <div>
    <CRow>
      <CCol :md="12">
        <CCard class="mb-4">
          <CCardBody>
            <CRow>
              <CCol :sm="5">
                <h4 id="traffic" class="card-title mb-0">Members</h4>
                <div class="small text-medium-emphasis">Oktober 2022</div>
              </CCol>
              <CTable align="middle" class="mb-0 border" hover responsive>
                <CTableHead color="light">
                  <CTableRow>
                    <CTableHeaderCell class="text-center"> # </CTableHeaderCell>
                    <CTableHeaderCell> Name / Role </CTableHeaderCell>
                    <CTableHeaderCell class="text-center"
                      >Email</CTableHeaderCell
                    >
                    <CTableHeaderCell class="text-center"
                      >Projects</CTableHeaderCell
                    >
                    <CTableHeaderCell class="text-center"
                      >Tickets</CTableHeaderCell
                    >
                    <CTableHeaderCell class="text-center"
                      >Action</CTableHeaderCell
                    >
                  </CTableRow>
                </CTableHead>
                <CTableBody>
                  <CTableRow
                    v-for="user in users"
                    v-bind:value="user.id"
                    v-bind:key="user.id"
                  >
                    <CTableDataCell class="text-center">
                      <div>{{ user.id }}</div>
                      <!-- <CAvatar
                       :key="case.name"
                        size="md"
                        :src="item.avatar.src"
                        :status="item.avatar.status"
                      /> -->
                    </CTableDataCell>
                    <CTableDataCell>
                      <div>
                        <!-- <a href="/" target="_blank" rel="noopener noreferrer" class="disabled" aria-disabled="true"></a> -->
                        {{ user.name }}
                      </div>
                      <div
                        class="small text-medium-emphasis text-truncate"
                        style="max-width: 250px"
                      >
                        {{ userRoles[user.user_role] }}
                      </div>
                    </CTableDataCell>
                    <CTableDataCell class="text-center">
                      <small>{{ user.email }}</small>
                    </CTableDataCell>
                    <CTableDataCell class="text-center">
                      <div class="text-medium-emphasis">
                        <CBadge color="success">{{
                          getProjectsByUser(user.id)
                        }}</CBadge>
                      </div>
                    </CTableDataCell>
                    <CTableDataCell class="text-center">
                      <div class="text-medium-emphasis">
                        <CBadge color="info">{{
                          getCasesByUser(user.id)
                        }}</CBadge>
                      </div>
                    </CTableDataCell>
                    <CTableDataCell class="text-center">
                      <div>
                        <AppOffcanvasMemberEdit v-bind:user="user" />
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
import axios from 'axios'
import AppOffcanvasMemberEdit from '../../components/AppOffcanvasMemberEdit.vue'

export default {
  name: 'MemberList',
  components: {
    AppOffcanvasMemberEdit,
  },
  data() {
    return {
      token: this.$store.state.token,
      apiURL: this.$store.state.apiURL,
      name: '',
      email: '',
      user_role: '',
      team_role: '',
      assign_date: '',
      active: '',
      note: '',
      projects: [],
      users: [],
      team_members: [],
      cases: [],
      userRoles: this.$store.state.userRoles,
    }
  },
  mounted() {
    document.title = 'Members | BugFlix'
    const headers = {
      Authorization: `Bearer ${this.token}`,
      'Content-Type': 'application/json',
    }
    axios
      .get(`${this.apiURL}/project`, { headers })
      .then((response) => {
        this.projects = response.data
      })
      .catch((error) => console.log(`${error}`))
    axios
      .get(`${this.apiURL}/user`, { headers })
      .then((response) => {
        this.users = response.data
      })
      .catch((error) => console.log(`${error}`))
    axios
      .get(`${this.apiURL}/team_member`, { headers })
      .then((response) => {
        this.team_members = response.data
      })
      .catch((error) => console.log(`${error}`))
    axios
      .get(`${this.apiURL}/case`, { headers })
      .then((response) => {
        this.cases = response.data
      })
      .catch((error) => console.log(`${error}`))
  },
  methods: {
    getProjectsByUser(userID) {
      let projectsByUser = 0
      for (let x = 0; x < this.team_members.length; x++) {
        if (this.team_members[x].user_id === userID) {
          projectsByUser++
        }
      }
      return projectsByUser
    },
    getCasesByUser(userID) {
      let casesByUser = 0
      for (let x = 0; x < this.cases.length; x++) {
        if (this.cases[x].owner_id === userID) {
          casesByUser++
        }
      }
      return casesByUser
    },
  },
}
</script>
