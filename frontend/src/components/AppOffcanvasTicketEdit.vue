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
      <COffcanvasTitle>Offcanvas731</COffcanvasTitle>
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
    {{ the_case }}
      <CForm @submit.prevent="submitTicket">
        <div class="mb-3">
          <CFormLabel for="title">Title:</CFormLabel>
          <CFormInput
            id="title"
            type="text"
            placeholder="Ticket Title"
            name="title"
            v-model="the_case.title"
          />
        </div>
        <div class="mb-3">
          <CFormLabel for="description"><b>Description:</b></CFormLabel>
          <CFormTextarea
            id="description"
            rows="3"
            v-model="the_case.description"
          ></CFormTextarea>
        </div>
        <div class="mb-3">
          <CFormLabel for="ticketType"><b>Ticket Type:</b></CFormLabel>
          <CFormSelect
            aria-label="Ticket Type"
            id="ticketType"
            name="ticketType"
          >
            <option v-for="(type_options,index) in case_type_options " :selected="the_case.case_type == index">
              {{ type_options }}
            </option>

            <!--
            v-model="the_case.case_type"
             <option value="1">Issue</option>
            <option value="2">Bug</option>
            <option value="3">Note</option>-->
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
            v-model="the_case.ticketPriority"
          >
            <!--<option v-for="case_options in case_type_options ">
              {# {{ case_options }} || {{ case_options }} #}
            </option>
             <option selected disabled>Priority</option>
            <option value="1">Normal</option>
            <option value="2">Medium</option>
            <option value="3">High</option>
            <option value="4">Critical</option> -->
          </CFormSelect>
        </div>
        <div class="mb-3">
          <CFormLabel for="ticketStatus"><b>Ticket Status:</b></CFormLabel>
          <CFormSelect
            aria-label="Ticket Status"
            id="ticketStatus"
            name="ticketStatus"
            v-model="the_case.ticketStatus"
          >
            <option value="1">New</option>
            <option value="2">In Progress</option>
            <option value="3">On Hold</option>
            <option value="4">Solved</option>
          </CFormSelect>
        </div>
        {# <div class="mb-3">
          <CFormLabel for="projectSelected"><b>Project:</b></CFormLabel>
          <CFormSelect
            aria-label="Project Selected"
            id="projectSelected"
            name="projectSelected"
            v-model="the_case.projectSelected"
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
        </div> #}
        {# <div class="mb-3">
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
        </div> #}
        <hr />
        <CCol :xs="12">
          <CButton color="primary" type="submit">Submit Ticket</CButton>
          <div class="vr"></div>
          <CButton color="secondary" type="submit">Cancel </CButton>
        </CCol>
      </CForm>
      
    </COffcanvasBody>
  </COffcanvas>
</template>
<script>
export default {
  // inject: ['all_cases'],
  props: ['the_case'],
  data() {
    return {
      visibleEnd: false,
      case_type_options: {
        '1': 'Issue',
        '2': 'Bug',
        '3': 'Note'      
      }
    }
  },
}
</script>
