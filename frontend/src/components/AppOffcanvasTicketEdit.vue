<template>
  <CButton
    color="primary"
    @click="
      () => {
        visibleEnd = !visibleEnd
      }
    "
    >Edit</CButton
  >
  <COffcanvas
    placement="end"
    :visible="visibleEnd"
    @hide="
      () => {
        visibleEnd = !visibleEnd
      }
    "
  >
    <COffcanvasHeader>
      <COffcanvasTitle>Ticket</COffcanvasTitle>
      <CCloseButton
        class="text-reset"
        @click="
          () => {
            visibleEnd = false
          }
        "
      />
    </COffcanvasHeader>
    <COffcanvasBody>
      {{ this.case }}
      <p>-------------------------------------</p>
      <CForm @submit.prevent="submitTicket">
        <div class="mb-3">
          <CFormLabel for="title">Title:</CFormLabel>
          <CFormInput
            id="title"
            type="text"
            placeholder="Ticket Title"
            name="title"
            v-model="this.case.title"
          />
        </div>
        <div class="mb-3">
          <CFormLabel for="description"><b>Description:</b></CFormLabel>
          <CFormTextarea
            id="description"
            rows="3"
            v-model="this.case.description"
          ></CFormTextarea>
        </div>
        <div class="mb-3">
          <CFormLabel for="ticketType"><b>Ticket Type:</b></CFormLabel>
          <CFormSelect
            aria-label="Ticket Type"
            id="ticketType"
            name="ticketType"
            v-model="ticketType"
          >
            <option
              v-for="(type_options, index) in case_type_options"
              v-bind:key="index"
              v-bind:value="index"
              :selected="this.case.case_type == index"
            >
              {{ type_options }}
            </option>
          </CFormSelect>
        </div>
        <div class="mb-3">
          <CFormLabel for="ticketPriority"><b>Ticket Priority:</b></CFormLabel>
          <CFormSelect
            aria-label="Ticket Priority"
            id="ticketPriority"
            name="ticketPriority"
            v-model="ticketPriority"
          >
            <option
              v-for="(priority_option, index) in priority_options"
              v-bind:key="index"
              v-bind:value="index"
              :selected="this.case.priority == index"
            >
              {{ priority_option }}
            </option>
          </CFormSelect>
        </div>
        <div class="mb-3">
          <CFormLabel for="ticketStatus"><b>Ticket Status:</b></CFormLabel>
          <CFormSelect
            aria-label="Ticket Status"
            id="ticketStatus"
            name="ticketStatus"
            v-model="ticketStatus"
          >
            <option
              v-for="(status_option, index) in caseStatus"
              v-bind:key="index"
              v-bind:value="index"
              :selected="this.case.status == index"
            >
              {{ status_option }}
            </option>
          </CFormSelect>
        </div>
        <div class="mb-3">
          <CFormLabel for="projectSelected"><b>Project:</b></CFormLabel>
          <CFormSelect
            aria-label="Project Selected"
            id="projectSelected"
            name="projectSelected"
            v-model="ticketProject"
          >
            <option
              v-for="projects in this.case.all_projects"
              :selected="this.case.project_id === projects.id"
              v-bind:key="projects.id"
              v-bind:value="projects.id"
            >
              {{ projects.title }}
            </option>
          </CFormSelect>
        </div>
        <div class="mb-3">
          <CFormLabel for="assigned"><b>Assign to:</b></CFormLabel>
          <CFormSelect id="assigned" name="assigned" v-model="ticketOwner">
            <option
              v-for="users in this.case.all_users"
              :selected="this.case.owner_id == users.id"
              v-bind:key="users.id"
              v-bind:value="users.id"
            >
              {{ users.name }}
            </option>
          </CFormSelect>
        </div>
        <hr />
        <CCol :xs="12">
          <CButton
            color="primary"
            type="submit"
            :visible="visibleEnd"
            @click="$emit('updateTicketList')"
            @hide="
              () => {
                visibleEnd = !visibleEnd
              }
            "
            >Edit Ticket</CButton
          >
          <div class="vr"></div>
          <CButton
            color="secondary"
            type="submit"
            @click.prevent="
              () => {
                visibleEnd = !visibleEnd
              }
            "
            >Cancel
          </CButton>
        </CCol>
      </CForm>
    </COffcanvasBody>
  </COffcanvas>
</template>

<script>
import axios from 'axios'
export default {
  props: ['the_case'],
  data() {
    return {
      case: this.the_case,
      // Store
      token: this.$store.state.token,
      apiURL: this.$store.state.apiURL,
      caseStatus: this.$store.state.status,
      casePriority: this.$store.state.priority,
      caseType: this.$store.state.case_type,
      visibleEnd: false,
      start_date: '',
      due_date: '',
      title: '',
      description: '',
      ticketStatus: '',
      ticketPriority: '',
      ticketProject: '',
      ticketOwner: '',
      projects: [],
      users: [],
      all_projects: [],
      all_users: [],
      ticketType: '',
      case_type_options: {
        1: 'Issue',
        2: 'Bug',
        3: 'Note',
      },
      status_options: {
        1: 'New',
        2: 'In Progress',
        3: 'On Hold',
        4: 'Solved',
      },
      priority_options: {
        1: 'Normal',
        2: 'Medium',
        3: 'High',
        4: 'Critical',
      },
    }
  },
  methods: {
    async submitTicket() {
      const case_data = {
        id: this.the_case.id,
        start_date: this.the_case.start_date,
        due_date: this.the_case.due_date,
        title: this.the_case.title,
        description: this.the_case.description,
        tags: 'test Tag',
        status: this.ticketStatus,
        priority: this.ticketPriority,
        case_type: this.ticketType,
        project_id: this.ticketProject,
        owner_id: this.ticketOwner,
      }
      const headers = {
        Authorization: `Bearer ${this.token}`,
        'Content-Type': 'application/json',
      }
      console.log('TICKET DATA: ', case_data)
      await axios
        .put(`${this.apiURL}/case/` + this.the_case.id, case_data, { headers })
        .then(
          (response) =>
            console.log('New Case: ' + JSON.stringify(response.data)),
          (this.visibleEnd = !this.visibleEnd),
        )
        .catch((error) => console.log(`${error}`))
      await axios
        .get(`${this.apiURL}/project`, { headers })
        .then((response) => {
          this.projects = response.data
          console.log('projects: ', this.projects)
        })
        .catch((error) => console.log(`${error}`))
      await axios
        .get(`${this.apiURL}/user`, { headers })
        .then((response) => {
          this.users = response.data
          console.log('User Names: ', this.users)
        })
        .catch((error) => console.log(`${error}`))
      return
    },
  },
}
</script>
