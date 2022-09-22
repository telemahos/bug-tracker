<template>
  <h1>New Ticket</h1>

  <CRow>
    <CCol :xs="12">
      <CCard class="mb-4">
        <CCardHeader>
          <strong>Create a new Ticket</strong>
        </CCardHeader>
        <CCardBody>
          <CForm @submit.prevent="submitTicket">
            <div class="mb-3 form-floating">
              <CFormLabel for="title"><b>Title:</b></CFormLabel>
              <CFormInput
                id="title"
                type="text"
                floatingLabel="Ticket Title"
                placeholder="Ticket Title"
                name="title"
                v-model="title"
              />
            </div>
            <div class="mb-3 form-floating">
              <CFormTextarea
                id="description"
                floatingLabel="Description"
                placeholder="Description"
                rows="3"
                style="height: 100px"
                v-model="description"
              ></CFormTextarea>
              <!-- <CFormLabel for="description"><b>Description:</b></CFormLabel> -->
            </div>
            <!-- Today and Due Date -->
            <div class="mb-3 form-check-inline">
              <label for="start_date">Today</label>
              <CFormInput
                id="start_date"
                type="text"
                placeholder="Today"
                name="start_date"
                v-model="start_date"
                readonly
              />
            </div>
            <div class="mb-3 form-check-inline">
              <label for="duedate">Due Date</label>
              <flat-pickr
                v-model="duedate"
                :config="config"
                class="form-control"
                placeholder="Due Date"
                name="duedate"
              >
              </flat-pickr>
            </div>
            <div class="mb-3">
              <CFormLabel for="ticketType"><b>Ticket Type:</b></CFormLabel>
              <CFormSelect
                aria-label="Ticket Type"
                id="ticketType"
                name="ticketType"
                v-model="ticketType"
              >
                <option selected disabled>Type</option>
                <option value="1">Issue</option>
                <option value="2">Bug</option>
                <option value="3">Note</option>
              </CFormSelect>
            </div>
            <div class="mb-3">
              <CFormLabel for="ticketPriority"
                ><b>Ticket Priority:</b></CFormLabel
              >
              <CFormSelect
                aria-label="Ticket Priority"
                id="ticketPriority"
                name="ticketPriority"
                v-model="ticketPriority"
              >
                <option selected disabled>Priority</option>
                <option value="1">Normal</option>
                <option value="2">Medium</option>
                <option value="3">High</option>
                <option value="4">Critical</option>
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
                <option value="1">New</option>
                <option value="2">In Progress</option>
                <option value="3">On Hold</option>
                <option value="4">Solved</option>
              </CFormSelect>
            </div>
            <div class="mb-3">
              <CFormLabel for="projectSelected"><b>Project:</b></CFormLabel>
              <CFormSelect
                aria-label="Project Selected"
                id="projectSelected"
                name="projectSelected"
                v-model="projectSelected"
              >
                <option selected disabled>Project</option>
                <option
                  v-for="project in projects"
                  v-bind:key="project.title"
                  v-bind:value="project.id"
                >
                  {{ project.title }}
                </option>
              </CFormSelect>
            </div>
            <div class="mb-3">
              <CFormLabel for="assigned"><b>Assign to:</b></CFormLabel>
              <CFormSelect
                aria-label="Assign"
                id="assigned"
                name="assigned"
                v-model="assigned"
              >
                <option selected disabled>Unassigned</option>
                <option v-for="user in users" :key="user.name" :value="user.id">
                  {{ user.name }} | {{ user.id }}
                </option>
              </CFormSelect>
            </div>
            <hr />
            <CCol :xs="12">
              <CButton color="primary" type="submit">Submit Ticket</CButton>
              <div class="vr"></div>
              <CButton color="secondary" type="submit">Cancel </CButton>
            </CCol>
          </CForm>
        </CCardBody>
      </CCard>
    </CCol>
  </CRow>
</template>

<script>
import axios from 'axios'
import flatPickr from 'vue-flatpickr-component'
import 'flatpickr/dist/flatpickr.css'

export default {
  name: 'TicketNew',
  components: {
    flatPickr,
  },
  data() {
    return {
      // today: '16-10-2020',
      duedate: null,
      start_date: '',
      today: this.$store.state.today,
      db_today: '',
      year: '',
      month: '',
      day: '',
      // Get more form https://flatpickr.js.org/options/
      config: {
        wrap: true, // set wrap to true only when using 'input-group'
        altFormat: 'd-m-Y',
        altInput: true,
        dateFormat: 'Y-m-d',
        //  locale: Greek, // locale for this instance only
      },
      // Store
      token: this.$store.state.token,
      apiURL: this.$store.state.apiURL,
      date: '',
      title: '',
      description: '',
      ticketStatus: '',
      ticketPriority: '',
      ticketType: '',
      projects: [],
      users: [],
      projectSelected: '',
      assigned: '',
    }
  },
  mounted() {
    this.year = this.today.getFullYear()
    this.day = this.today.getDate()
    this.month = this.today.getMonth() + 1

    console.log('TODAY:', this.day + '-' + this.month + '-' + this.year)

    if (parseInt(this.month) <= 9) {
      this.month = '0' + this.month
    }
    if (parseInt(this.day) <= 9) {
      this.day = '0' + this.day
    }
    this.start_date = this.day + '-' + this.month + '-' + this.year
    this.db_today = this.year + '-' + this.month + '-' + this.day
    const headers = {
      Authorization: `Bearer ${this.token}`,
      'Content-Type': 'application/json',
    }
    axios
      .get(`${this.apiURL}/project`, { headers })
      .then((response) => {
        this.projects = response.data
        console.log('Projects', this.projects)
      })
      .catch((error) => console.log(`${error}`))
    axios
      .get(`${this.apiURL}/user`, { headers })
      .then((response) => {
        this.users = response.data
        console.log('Users', this.users)
      })
      .catch((error) => console.log(`${error}`))
  },
  methods: {
    async submitTicket() {
      const case_data = {
        id: 0,
        start_date: this.db_today,
        // start_date: "2022-09-13",
        // today: "2022-09-13",
        due_date: this.duedate,
        title: this.title,
        description: this.description,
        tags: 'test Tag',
        status: this.ticketStatus,
        priority: this.ticketPriority,
        case_type: this.ticketType,
        project_id: this.projectSelected,
        owner_id: this.assigned,
        // project_id: 1,
        // owner_id: 2,
      }
      const headers = {
        Authorization: `Bearer ${this.token}`,
        'Content-Type': 'application/json',
      }
      console.log('TICKET DATA: ', case_data)
      await axios
        .post(`${this.apiURL}/case`, case_data, { headers })
        .then((response) =>
          console.log('New Case: ' + JSON.stringify(response.data)),
        )
        .catch((error) => console.log(`${error}`))
    },
  },
}
</script>
