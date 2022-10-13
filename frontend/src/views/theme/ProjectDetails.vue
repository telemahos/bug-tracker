<template>
  <CRow>
    <CCol :xs="12">
      <CCallout color="secondary" class="bg-white">
        <h4>{{ project.title }}</h4>
        <div class="">
          <dl class="row">
            <dd
              class="col-sm-12 d-flex w-75 justify-content-between align-items-center"
            >
              Create Date :<em class="text-muted"> {{ project.start_date }}</em
              ><span class="text-muted">|</span>Due Date :<em
                class="text-muted"
              >
                {{ project.due_date }}</em
              ><span class="text-muted">|</span><span>Priority:</span
              ><CBadge color="danger">{{
                projectPriority[project.priority]
              }}</CBadge
              ><span class="text-muted">|</span><span>Status:</span
              ><span class="text-success"
                ><em>{{ projectStatus[project.status] }}</em></span
              >
            </dd>
          </dl>
        </div>
      </CCallout>
    </CCol>
    <CCol :lg="4">
      <CCard class="mb-4">
        <CCardHeader> <strong></strong> <small>DETAILS</small> </CCardHeader>
        <CCardBody>
          <CListGroup>
            <CListGroupItem
              class="d-flex justify-content-between align-items-center"
            >
              Project No.
              <small>{{ project.project_nr }}</small>
            </CListGroupItem>
            <CListGroupItem>
              <div class="d-flex w-100 justify-content-between">
                <h6 class="mb-1">Title</h6>
                <small>{{ project.title }}</small>
              </div>
            </CListGroupItem>
            <CListGroupItem>
              <div class="d-flex w-100 justify-content-between">
                <h6 class="mb-1">Priority</h6>
                <CBadge color="danger">{{
                  projectPriority[project.priority]
                }}</CBadge>
              </div>
            </CListGroupItem>
            <CListGroupItem>
              <div class="d-flex w-100 justify-content-between">
                <h6 class="mb-1">Status</h6>
                <small class="text-info">{{
                  projectStatus[project.status]
                }}</small>
              </div>
            </CListGroupItem>
            <CListGroupItem>
              <div class="d-flex w-100 justify-content-between">
                <h6 class="mb-1">Start Date</h6>
                <small>{{ project.start_date }}</small>
              </div>
            </CListGroupItem>
            <CListGroupItem>
              <div class="d-flex w-100 justify-content-between">
                <h6 class="mb-1">Due Date</h6>
                <small>{{ project.due_date }}</small>
              </div>
            </CListGroupItem>
          </CListGroup>
        </CCardBody>
      </CCard>
      <CCard class="mb-4">
        <CCardHeader>
          <div class="d-flex w-100 justify-content-between align-items-center">
            <small class="">TEAM MEMBERS</small>
            <span class="text-end"
              ><CButton color="primary" variant="ghost" class="btn-sm"
                >Invite+</CButton
              ></span
            >
          </div>
        </CCardHeader>
        <CCardBody>
          <CListGroup>
            <CListGroupItem
              class="row row-cols-2"
              v-for="team_member in team_members"
              v-bind:key="team_member.id"
            >
              <div
                class="d-flex w-100 justify-content-between align-items-center"
              >
                <h6 class="col mb-1">{{ team_member.name }}</h6>
                <small>
                  <span class="col text-muted text-right">{{
                    userRoles[team_member.user_role]
                  }}</span></small
                >
                <hr />
              </div>
            </CListGroupItem>
          </CListGroup>
        </CCardBody>
      </CCard>
    </CCol>
    <CCol :lg="8">
      <CCard class="mb-4">
        <CCardHeader> <strong></strong> <small>OVERVIEW</small> </CCardHeader>
        <CCardBody>
          <p class="text-medium-emphasis">
            {{ project.description }}
          </p>
        </CCardBody>
      </CCard>
      <CCard class="mb-4">
        <CCardHeader>
          <div class="d-flex w-100 justify-content-between align-items-center">
            <small>COMMENTS</small>
            <span class="text-end"
              ><CButton color="primary" variant="ghost" class="btn-sm"
                >Add Comment</CButton
              ></span
            >
          </div>
        </CCardHeader>
        <CCardBody>
          <CCard class="">
            <CCardBody>
              <!-- <CCardTitle>Card title</CCardTitle> w-75-->
              <CCardSubtitle
                >Kakoulis Kostas
                <small class="text-muted"
                  >20 Dec 2021 - 05:47AM</small
                ></CCardSubtitle
              >
              <CCardText>
                <p class="text-medium-emphasis small">
                  I am getting message from customers that when they place order
                  always get error message .
                </p>
                <!-- <p><CCardLink>Edit</CCardLink></p> -->
              </CCardText>
              <!-- <CButton href="#">Go somewhere</CButton> -->
            </CCardBody>
          </CCard>
          <CCard class="">
            <CCardBody>
              <!-- <CCardTitle>Card title</CCardTitle> w-75-->
              <CCardSubtitle
                >Panagiotidou Noula
                <small class="text-muted"
                  >20 Dec 2021 - 05:47AM</small
                ></CCardSubtitle
              >
              <CCardText>
                <p class="text-medium-emphasis small">
                  I am getting message from customers that when they place order
                  always get error message .
                </p>
                <p><CCardLink>Edit</CCardLink></p>
              </CCardText>
              <!-- <CButton href="#">Go somewhere</CButton> -->
            </CCardBody>
          </CCard>
        </CCardBody>
      </CCard>
    </CCol>
  </CRow>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ProjectDetails',
  props: ['id'],
  data() {
    return {
      projectID: this.id,
      token: this.$store.state.token,
      apiURL: this.$store.state.apiURL,
      project: '',
      project_nr: '',
      start_date: '',
      due_date: '',
      title: '',
      description: '',
      projectStatus: this.$store.state.status,
      projectPriority: this.$store.state.priority,
      projectType: this.$store.state.case_type,
      userRoles: this.$store.state.userRoles,
      users: [],
      members: [],
      team_members: [],
    }
  },
  beforeMount() {
    this.loadProject()
    this.loadUsersAndProjects()
  },
  mounted() {
    document.title = 'Project Overview | BugFlix'
  },
  methods: {
    async loadProject() {
      const headers = {
        Authorization: `Bearer ${this.token}`,
        'Content-Type': 'application/json',
      }
      await axios
        .get(`${this.apiURL}/project/` + this.projectID, { headers })
        .then((response) => {
          this.project = response.data
          // console.log('This PROJECT: ', this.project)
        })
        .catch((error) => console.log(`${error}`))
    },
    async loadUsersAndProjects() {
      const headers = {
        Authorization: `Bearer ${this.token}`,
        'Content-Type': 'application/json',
      }
      // await axios
      //   .get(`${this.apiURL}/project/`, { headers })
      //   .then((response) => {
      //     this.projects = response.data
      //     // console.log('projects77: ', this.projects)
      //   })
      //   .finally(() => {
      //     for( let x = 0; x < this.projects.length; x++ ) {
      //       if ( this.case.project_id == this.projects[x].id ){
      //         // console.log('PID: ', this.projects[x].id)
      //         this.project = this.projects[x]
      //       }
      //     }
      //   })
      //   .catch((error) => console.log(`${error}`))
      await axios
        .get(`${this.apiURL}/user`, { headers })
        .then((response) => {
          this.users = response.data
          // console.log('User Names: ', this.users)
        })
        .catch((error) => console.log(`${error}`))
      await axios
        .get(`${this.apiURL}/team_member`, { headers })
        .then((response) => {
          this.members = response.data
          // console.log('MEMBER Names: ', this.members)
        })
        .finally(() => {
          let z = 0
          for (let x = 0; x < this.members.length; x++) {
            if (this.project.id == this.members[x].project_id) {
              this.team_members[z] = this.users[this.members[x].id]
              // console.log('TEAM: ', this.team_members[z])
              z++
            }
          }
        })
        .catch((error) => console.log(`${error}`))
    },
  },
}
</script>
