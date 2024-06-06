<script context="module" lang="ts">
    import { type SvelteComponent } from 'svelte';
    import type { ListItemData } from '../../lib/search/ListItem.svelte'
</script>

<script lang="ts">
    import { onMount } from 'svelte';
    import { get_token } from '../../stores/auth';

    import FolderIcon from "../../assets/folderIcon.svg"
    import CertificateIcon from "../../assets/certificate.svg";

    import HeroSection from "../../lib/sections/HeroSection.svelte";
    import LoadingIcon from '../../lib/ui/LoadingIcon.svelte';
    import ErrorModal from '../../lib/ui/ErrorModal.svelte';
    import SearchList from "../../lib/search/SearchList.svelte";
    import DateSelect from '../../lib/dates/DateSelect.svelte';
    import ImportantBtn from '../../lib/ui/ImportantBtn.svelte';
    import FooterLarge from '../../lib/sections/FooterLarge.svelte';
    
    import Selected from "./Selected.svelte";

    const SERVER_IP = import.meta.env.VITE_API_SERVER_IP;

    const navLinks = [
        {displayName: "Home", url: `/`},
        {displayName: "About", url: `/about`},
        {displayName: "Logout", url: `/logout`},
    ]

    let certData: ListItemData[] = [];

    let dkdmData: ListItemData[] = [];

    let showLoading = false;

    let errorModal: SvelteComponent;
    let selectedCertElem: SvelteComponent;
    let selectedDKDMElem: SvelteComponent;
    let selectedCertValue: ListItemData | null = null; 
    let selectedDKDMValue: ListItemData | null = null;

    let startDateComp: SvelteComponent;
    let endDateComp: SvelteComponent;
    let timezoneComp: SvelteComponent;

    function showError(e: string): void {
        errorModal.setError(e);
        errorModal.show();
    }

    function closeError() {
        errorModal.hide();
    }

    onMount(() => {
        getRequest('/api/get_user_certs').then(res => {
            certData = res;
        });

        getRequest('/api/get_user_dkdms').then(res => {
            dkdmData = res;
        });
    });

    function downloadLeaf() {
        window.open(`${SERVER_IP}/api/public_leaf`, '_blank');
    }

    async function getRequest(endpoint: string): Promise<any> {
        try{
            let res = await fetch(`${SERVER_IP}${endpoint}`, {
                method: 'GET',                
                headers: {
                    'Authorization': `Token ${get_token()}`
                }
            });
            let data = await res.json();
            
            if (res.ok) {
                let formattedData: any = [];
                data.forEach((item: any) => {
                    item['isFile'] = true;
                    item['isDir'] = false;
                    formattedData.push(item);
                });
                return formattedData;
            } else {
                if (data.detail) {
                    showError(`${data.detail}`);
                } else {
                    showError(`Failed to get data: ${res.status}`);
                }
            }
        } catch (e) {
            showError(`Failed GET Request: ${e}`);
        }
    }

    async function deleteRequest(endpoint: string): Promise<void> {
        try {
            let res = await fetch(`${SERVER_IP}${endpoint}`, {
                method: 'DELETE',
                headers: {
                    'Authorization': `Token ${get_token()}`
                }
            });
            let data = await res.json();

            if (!res.ok) {
                if (data.detail) {
                    showError(`${data.detail}`);
                } else {
                    showError(`Failed to delete file: ${res.status}`);
                }
            }
        } catch (e) {
            showError(`Failed to delete file: ${e}`);
        }
    }


    async function uploadFile(file: File, endpoint: string): Promise<void> {
        let formData = new FormData();
        formData.append('file', file);

        try {
            let res = await fetch(`${SERVER_IP}${endpoint}`, {
                method: 'POST',
                body: formData,
                headers: {
                    'Authorization': `Token ${get_token()}`
                }
            });
            let data = await res.json();

            if (!res.ok) {
                if (data.detail) {
                    showError(`${data.detail}`);
                } else {
                    showError(`Failed to upload file: ${res.status}`);
                }
            }
        } catch (e) {
            showError(`Failed to upload file: ${e}`);
        }
    }

    async function deleteCert(e: CustomEvent) {
        let endpoint = `/api/certs/${e.detail.data.id}`;
        await deleteRequest(endpoint);
        getRequest('/api/get_user_certs').then(res => {
            certData = res;
        });
    }

    async function deleteDKDM(e: CustomEvent) {
        let endpoint = `/api/dkdms/${e.detail.data.id}`;
        await deleteRequest(endpoint);
        getRequest('/api/get_user_dkdms').then(res => {
            dkdmData = res;
        });
    }

    async function uploadCert(e: CustomEvent) {
        if (!e.detail.file) return;
        await uploadFile(e.detail.file, '/api/add_user_cert');
        getRequest('/api/get_user_certs').then(res => {
            certData = res;
        });
    }

    async function uploadDKDM(e: CustomEvent) {
        if (!e.detail.file) return;
        await uploadFile(e.detail.file, '/api/add_user_dkdm');
        getRequest('/api/get_user_dkdms').then(res => {
            dkdmData = res;
        });
    }

    async function submit() {
        console.log(selectedCertValue);
        // startDateComp.clearError();
        // endDateComp.clearError();
        // selectedCertElem.clearError();
        // selectedDKDMElem.clearError();

        // if (!selectedCertValue) {
        //     selectedCertElem.setError();
        // }

        // if (!selectedDKDMValue) {
        //     selectedDKDMElem.setError();
        // }        

        // let start = startDateComp.getValue();
        // if (!start) {
        //     startDateComp.setError();
        // }

        // let end = endDateComp.getValue();
        // if (!end) {
        //     endDateComp.setError();
        // }

        // if (!(
        //     selectedCertValue &&
        //     selectedDKDMValue &&
        //     start && end
        // )) {
        //     return;
        // }
        
        // let tz = timezoneComp.getValue();

        // let data = {
        //     "cert": selectedCertValue,
        //     "dkdm": selectedDKDMValue.display_name,
        //     "startDate": start,
        //     "endDate": end,
        //     "timezone": tz,
        // }

        // showLoading = true;
        // coms.submitJSON('/api/kdm/submit', data).then(res => {
        //     console.log(res.status);
        //     // updateHistory();
        //     showLoading = false;
        // });
    }
</script>

<svelte:head>
    <title>Generate</title>
</svelte:head>

<main id="main">
    <div class="hidden">
        <LoadingIcon width="30px" height="30px"/>
    </div>
    <ErrorModal bind:this={errorModal} on:click={closeError}/>
    <HeroSection navLinks={navLinks} paddingTop="100px">
        <div class="certSection">
            <div style="width: 40%">
                <SearchList listData={certData}
                    on:fileAdded={uploadCert}
                    on:searchItemDeleted={deleteCert}
                    bind:selected={selectedCertValue}
                    header="Certificate"
                    boxHeight="200px"
                    searchPlaceholder="Search Certs"
                    fileIcon={CertificateIcon}
                    dirIcon={FolderIcon}
                    filetypes=".pem,.crt,.cer"
                />
                <Selected bind:this={selectedCertElem} selected={selectedCertValue}/>
            </div>
            <div style="width: 40%">
                <SearchList listData={dkdmData}
                    on:fileAdded={uploadDKDM}
                    on:searchItemDeleted={deleteDKDM}
                    bind:selected={selectedDKDMValue}
                    header="CPL DKDM"
                    boxHeight="200px"
                    searchPlaceholder="Search CPLs"
                    fileIcon={CertificateIcon}
                    dirIcon={FolderIcon}
                    filetypes=".xml"
                />
                <Selected bind:this={selectedDKDMElem} selected={selectedDKDMValue}/>
            </div>
        </div>
    </HeroSection>
    <section class="dateSection">
        <div class="sectionContainer">
            <div class="dateContainer">
                <DateSelect bind:this={startDateComp} header="Start"/>
                <DateSelect bind:this={endDateComp} header="End"/>
                <DateSelect bind:this={timezoneComp} isTimezone={true} header="Timezone"/>
            </div>
            <div class="outputContainer">
                <ImportantBtn
                    on:click={downloadLeaf}
                    content="Get Certificate"
                    fontSize="12pt"
                    padding="10px 55px"
                    margin="0px 00px"
                />
                {#if showLoading}
                    <LoadingIcon width="30px" height="30px"/>
                {:else}
                    <ImportantBtn
                        on:click={submit}
                        content="Generate KDM"
                        fontSize="12pt"
                        padding="10px 55px"
                    />
                {/if}
            </div>
        </div>
    </section>
    <div class="footerContainer">
        <FooterLarge navLinks={navLinks} paddingTop="30px" showBorder={false}/>
    </div>
</main>

<style>
    main {
        font-family: "Montserrat";
        min-width: 900px;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
    }

    .certSection {
        display: flex;
        justify-content: space-around;
        gap: 20px;
        max-width: 80%;
        margin-left: auto;
        margin-right: auto;
    }

    .sectionContainer {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        width: 80%;
        margin-left: auto;
        margin-right: auto;
        gap: 20px;
    }

    .dateSection {
        padding: 20px 0px;
        width: 100%;
        background: linear-gradient(310deg, #125a64 0%, #572360b9 99%);
    }
    .dateContainer {
        display: flex;
        justify-content: center;
        width: 100%;
        gap: 4%;
        margin-left: auto;
        margin-right: auto;
    }

    .outputContainer {
        margin-top: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        padding: 5px;
        gap: 5%;
    }

    .footerContainer {
        margin-top: auto;
        background: linear-gradient(310deg, #122c30 0%, #0f2e36 99%);
        padding-bottom: 10px;
    }

    .hidden {
        display: none;
    }
</style>