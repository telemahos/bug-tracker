<template>
  <h1 class="mb-8">
    {{ this.case.title }}
    <small class="text-muted"></small>
  </h1>

  <CRow>
    <CCol :xs="12">
      <!-- <DocsCallout name="Badges" href="components/badge.html" />-->
    </CCol>
    <CCol :lg="4">
      <CCard class="mb-4">
        <CCardHeader> <strong></strong> <small>DETAILS</small> </CCardHeader>
        <CCardBody>
          <CListGroup>
            <CListGroupItem
              class="d-flex justify-content-between align-items-center"
            >
              Case No.
              <small>{{ this.case.case_nr }}</small>
            </CListGroupItem>
            <CListGroupItem>
              <div class="d-flex w-100 justify-content-between">
                <h6 class="mb-1">Title</h6>
                <small>{{ this.case.title }}</small>
              </div>
            </CListGroupItem>
            <CListGroupItem>
              <!-- his.projects[this.projects.id]  this.case.project_id -->
              <div class="d-flex w-100 justify-content-between">
                <h6 class="mb-1">Project</h6>
                <small>{{ project.title }}</small>
              </div>
            </CListGroupItem>
            <CListGroupItem>
              <div class="d-flex w-100 justify-content-between">
                <h6 class="mb-1">Type</h6>
                <small class="text-dark">{{
                  ticketType[this.case.case_type]
                }}</small>
              </div>
            </CListGroupItem>
            <CListGroupItem>
              <div class="d-flex w-100 justify-content-between">
                <h6 class="mb-1">Priority</h6>
                <CBadge color="danger">{{
                  ticketPriority[this.case.priority]
                }}</CBadge>
              </div>
            </CListGroupItem>
            <CListGroupItem>
              <div class="d-flex w-100 justify-content-between">
                <h6 class="mb-1">Status</h6>
                <small class="text-info">{{
                  ticketStatus[this.case.status]
                }}</small>
              </div>
            </CListGroupItem>
            <CListGroupItem>
              <div class="d-flex w-100 justify-content-between">
                <h6 class="mb-1">Due Date</h6>
                <!-- <small>Sep 28, 2022</small> -->
                <small>{{ this.case.due_date }}</small>
              </div>
            </CListGroupItem>
          </CListGroup>
        </CCardBody>
      </CCard>
      <CCard class="mb-4">
        <CCardHeader>
          <strong></strong> <small>ASSIGNED TO</small>
        </CCardHeader>
        <CCardBody>
          <CListGroup>
            <CListGroupItem class="row row-cols-2">
              <div
                class="d-flex w-100 justify-content-between align-items-center"
              >
                <p class="col mb-1">{{ user.name }}</p>
                <small>
                  <span class="col text-muted">{{
                    userRoles[user.user_role]
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
        <CCardHeader>
          <strong></strong> <small>DESCRIPTION</small>
        </CCardHeader>
        <CCardBody>
          <p class="text-medium-emphasis">
            {{ this.case.description }}
          </p>
        </CCardBody>
      </CCard>
      <CCard class="mb-4">
        <CCardHeader> <strong></strong> <small>COMMENTS</small> </CCardHeader>
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
                >Paulie Durber
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
// import avatar from '@/assets/images/avatars/2.jpg'
import axios from 'axios'
export default {
  name: 'ticketdetails',
  props: ['id'],
  data() {
    return {
      caseID: this.id,
      token: this.$store.state.token,
      apiURL: this.$store.state.apiURL,
      case: '',
      case_nr: '',
      start_date: '',
      due_date: '',
      title: '',
      description: '',
      ticketStatus: this.$store.state.status,
      ticketPriority: this.$store.state.priority,
      ticketType: this.$store.state.case_type,
      userRoles: this.$store.state.userRoles,
      projects: '',
      users: [],
      user: '',
      project: '',
    }
  },
  beforeMount() {
    this.loadCase()
    this.loadUsersAndProjects()
  },
  mounted() {
    document.title = 'Ticket Overview | BugFlix'
  },
  methods: {
    async loadCase() {
      const headers = {
        Authorization: `Bearer ${this.token}`,
        'Content-Type': 'application/json',
      }
      await axios
        .get(`${this.apiURL}/case/` + this.caseID, { headers })
        .then((response) => {
          this.case = response.data
          // console.log('This CASE: ', this.case)
        })
        .catch((error) => console.log(`${error}`))
    },
    async loadUsersAndProjects() {
      const headers = {
        Authorization: `Bearer ${this.token}`,
        'Content-Type': 'application/json',
      }
      await axios
        .get(`${this.apiURL}/project/`, { headers })
        .then((response) => {
          this.projects = response.data
          // console.log('projects77: ', this.projects)
        })
        .finally(() => {
          for (let x = 0; x < this.projects.length; x++) {
            if (this.case.project_id == this.projects[x].id) {
              // console.log('PID: ', this.projects[x].id)
              this.project = this.projects[x]
            }
          }
        })
        .catch((error) => console.log(`${error}`))
      await axios
        .get(`${this.apiURL}/user`, { headers })
        .then((response) => {
          this.users = response.data
          // console.log('User Names: ', this.users)
        })
        .finally(() => {
          for (let x = 0; x < this.users.length; x++) {
            if (this.case.owner_id == this.users[x].id) {
              // console.log('OWNERID: ', this.users[x].id)
              this.user = this.users[x]
            }
          }
        })
        .catch((error) => console.log(`${error}`))
    },
  },
}
</script>
