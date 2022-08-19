<template>
  <h1>New Ticket</h1>

  <CRow>
    <!-- <CCol :xs="12">
      <DocsCallout name="Form Control" href="forms/form-control.html" />
    </CCol> -->
    <CCol :xs="12">
      <CCard class="mb-4">
        <CCardHeader>
          <strong>Create a new Ticket</strong>
        </CCardHeader>
        <CCardBody>
          <CForm @submit.prevent="submitTicket">
            <div class="mb-3">
              <CFormLabel for="exampleFormControlInput1"
                ><b>Title:</b></CFormLabel
              >
              <CFormInput
                id="exampleFormControlInput1"
                type="text"
                placeholder="Title"
              />
            </div>
            <div class="mb-3">
              <CFormLabel for="exampleFormControlTextarea1"
                ><b>Description:</b></CFormLabel
              >
              <CFormTextarea
                id="exampleFormControlTextarea1"
                rows="3"
              ></CFormTextarea>
            </div>
            <div class="mb-3">
              <CFormLabel for=""><b>Ticket Type:</b></CFormLabel>
              <CFormSelect aria-label="Default select example">
                <option>Type</option>
                <option value="1">Issue</option>
                <option value="2">Bug</option>
                <option value="3">Three</option>
              </CFormSelect>
            </div>
            <div class="mb-3">
              <CFormLabel for=""><b>Ticket Priority:</b></CFormLabel>
              <CFormSelect aria-label="Default select example">
                <option>Priority</option>
                <option value="1">Normal</option>
                <option value="2">Medium</option>
                <option value="3">High</option>
                <option value="4">Critical</option>
              </CFormSelect>
            </div>
            <div class="mb-3">
              <CFormLabel for=""><b>Ticket Status:</b></CFormLabel>
              <CFormSelect aria-label="Default select example">
                <option>Status</option>
                <option value="1">New</option>
                <option value="2">In Progress</option>
                <option value="3">On Hold</option>
                <option value="4">Solved</option>
              </CFormSelect>
            </div>
            <div class="mb-3">
              <CFormLabel for=""><b>Assign to:</b></CFormLabel>
              <CFormSelect aria-label="Default select example">
                <option>Unassigned</option>
                <option value="1">Kostas Kakoulis</option>
                <option value="2">Noula Kakouli</option>
                <option value="3">Niki Kakouli</option>
                <option value="4">Dev1</option>
              </CFormSelect>
            </div>
            <CCol :xs="12">
              <CButton color="primary" type="submit">Submit Ticket</CButton>

              <CButton color="secondary" type="submit">Cancel </CButton>
            </CCol>
          </CForm>
        </CCardBody>
      </CCard>
    </CCol>
  </CRow>
</template>

<script>
export default {
  name: 'AddTicket',
  components: {},
  data() {
    return {}
  },
  methods: {
    submitTicket() {
      const shift_data = {
        // id: 0,
        // service_id_1: waitressName1.value,
        // service_id_2: waitressName2.value,
        // barman_id_1: barmanName1.value,
        // barman_id_2: barmanName2.value
      }

      const headers = {
        // 'Authorization': `Bearer ${this.token}`,
        // 'Content-Type': 'application/json',
        // 'Content-Type': 'application/x-www-form-urlencoded',
      }
      // console.log("SHIFT DATA: ", shift_data)
      // await axios.post(
      //   `${this.apiURL}/shift`, shift_data, { headers })
      //   .then(response =>
      //     this.new_shift_id = response.data.id,
      //   )
      //   .catch((error) => console.log(`${error}`))
      //   .finally(() =>
      //     this.setIncome(this.new_shift_id)
      // );

      // console.log("new_shift_id22: " + this.new_shift_id);
    },
  },
}
</script>
