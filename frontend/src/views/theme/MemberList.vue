<template>
  <h1>This is MemberList Page!</h1>

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
                    <CTableHeaderCell class="text-center">
                      #
                    </CTableHeaderCell>
                    <CTableHeaderCell>
                      Name / Role
                    </CTableHeaderCell>
                    <CTableHeaderCell class="text-center"
                      >Email</CTableHeaderCell
                    >
                    <CTableHeaderCell>Projects</CTableHeaderCell>
                    <CTableHeaderCell>Tickets</CTableHeaderCell>
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
                        <a href="#" target="_blank" rel="noopener noreferrer">{{
                          user.name
                        }}</a>
                      </div>
                      <div
                        class="small text-medium-emphasis text-truncate"
                        style="max-width: 250px"
                      >
                        {{ role[user.user_role -1] }}
                      </div>
                    </CTableDataCell>
                    <CTableDataCell class="text-center">
                      <div>{{ user.email }}</div>
                    </CTableDataCell>
                    <CTableDataCell class="text-center">
                      <div class="small text-medium-emphasis">
                        <CBadge color="success">{{ getProjectsByUser(user.id) }}</CBadge>
                      </div>
                    </CTableDataCell>
                    <CTableDataCell>
                      <div
                        class="small text-secondary"
                        color="text-secondary"
                      >
                      ROLE: {{ user.user_role - 1 }}
                        {{ role[user.user_role - 1] }}
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

import axios from 'axios'
// import AppOffcanvasTicketEdit from '../../components/AppOffcanvasTicketEdit.vue'

export default {
  name: 'MemberList',
  components: {},
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
      role: ['Admin', 'Developer', 'QA Analyst', 'Business Analyst', 'Product Manager', 'Technology Manager'],
      // projectsByUser: '',
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
        // this.$store.commit('setProjects', this.projects)
        // console.log('Projects: ', this.projects)
      })
      .catch((error) => console.log(`${error}`))
    axios
      .get(`${this.apiURL}/user`, { headers })
      .then((response) => {
        this.users = response.data
        // this.$store.commit('setUsers', this.users)
        // console.log('Users: ', this.users)
      })
      .catch((error) => console.log(`${error}`))
    axios
      .get(`${this.apiURL}/team_member`, { headers })
      .then((response) => {
        this.team_members = response.data
        // this.$store.commit('setProjects', this.projects)
        // console.log('Team Members: ', this.team_members)
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
    }
  },
}
</script>
