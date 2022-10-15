<template>
  <div>
    <CCol :xs="12">
      <CCallout color="secondary" class="bg-white">
        <h4>My Dashboard</h4>
        <div class="">
          <p>
            This web app is still in development. Template is based on CoreUI.
            Backend is based on Python FastAPI and SQLite. All data is provided
            by the API, that you can find at:
            <a href="http://www.bugflix.eu:8000/docs" target="_blank"
              >bugflix.eu:8000/docs</a
            >
          </p>
          <p>Widgets are under construction...</p>
        </div>
      </CCallout>
    </CCol>
    <h1></h1>

    <WidgetTypeColorA />
    <WidgetCardA />
    <WidgetsStatsA />
    <WidgetsStatsD />
  </div>
</template>

<script>
import axios from 'axios'
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
      caseStatus: this.$store.state.status,
      casePriority: this.$store.state.priority,
      caseType: this.$store.state.case_type,
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
      all_projects: [],
      all_users: [],
      projectName: '',
      projectOwner: '',
    }
  },
  beforeMount() {
    // this.loadProject()
    // this.loadUsersAndProjects()
  },
  mounted() {
    document.title = 'My Dashboard | BugFlix'
    this.loadData()
  },
  methods: {
    async loadData() {
      const headers = {
        Authorization: `Bearer ${this.token}`,
        'Content-Type': 'application/json',
      }
      await axios
        .get(`${this.apiURL}/project`, { headers })
        .then((response) => {
          this.projects = response.data
          // this.$store.commit('setProjects', this.projects)
          // console.log('projects: ', this.projects)
        })
        .catch((error) => console.log(`${error}`))
      await axios
        .get(`${this.apiURL}/user`, { headers })
        .then((response) => {
          this.users = response.data
          // this.$store.commit('setUsers', this.users)
          // console.log('User Names: ', this.users)
        })
        .catch((error) => console.log(`${error}`))
      await axios
        .get(`${this.apiURL}/case`, { headers })
        .then((response) => {
          this.cases = response.data
          // console.log('Cases: ', this.cases)
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
          }
        })
        .catch((error) => console.log(`${error}`))
    },
  },
}
</script>
