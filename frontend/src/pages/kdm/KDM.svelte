<script context="module" lang="ts">
    import { onMount, type SvelteComponent } from 'svelte';
    import type { ListItemData } from '../../lib/search/ListItem.svelte'

    import * as coms from '../../lib/coms';
</script>

<script lang="ts">
    import { navigate } from 'svelte-routing';

    import FolderIcon from "../../assets/folderIcon.svg"
    import CertificateIcon from "../../assets/certificate.svg";

    import HeroSection from "../../lib/sections/HeroSection.svelte";
    import LoadingIcon from '../../lib/ui/LoadingIcon.svelte';
    import ErrorModal from '../../lib/ui/ErrorModal.svelte';
    import SearchList from "../../lib/search/SearchList.svelte";
    import DateSelect from '../../lib/dates/DateSelect.svelte';
    import ImportantBtn from '../../lib/ui/ImportantBtn.svelte';
    import FooterLinks from '../../lib/sections/FooterLinks.svelte';
    
    import Selected from "./Selected.svelte";

    const SERVER_IP = import.meta.env.VITE_API_SERVER_IP;

    const navLinks = [
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
    let outputDirComp: SvelteComponent;

    onMount(() => {
        
    });

    function showError(e: CustomEvent): void {
        errorModal.setError(e.detail);
        errorModal.show();
    }

    function closeError() {
        errorModal.hide();
    }

    async function test(e: CustomEvent) {
        if (!e.detail.file) return;
        let formData = new FormData();
        formData.append('file', e.detail.file);

        try {
            let res = await fetch(`${SERVER_IP}/api/test_post`, {
                method: 'POST',
                body: formData,
                credentials: 'include'
            });
            if (res.ok) {
                let data = await res.json();
                console.log(data);
            } else {
                showError(new CustomEvent('error', {detail: `Failed to upload cert: ${res.status}`}));
            }
        } catch (e) {
            showError(new CustomEvent('error', {detail: 'Failed to fetch certs'}));
        }
    }

    async function submit() {
        startDateComp.clearError();
        endDateComp.clearError();
        selectedCertElem.clearError();
        selectedDKDMElem.clearError();

        if (!selectedCertValue) {
            selectedCertElem.setError();
        }

        if (!selectedDKDMValue) {
            selectedDKDMElem.setError();
        }        

        let start = startDateComp.getValue();
        if (!start) {
            startDateComp.setError();
        }

        let end = endDateComp.getValue();
        if (!end) {
            endDateComp.setError();
        }

        let outputDir = outputDirComp.getValue();
        if (!outputDir) {
            outputDirComp.setError();
        }

        if (!(
            selectedCertValue &&
            selectedDKDMValue &&
            start && end && outputDir
        )) {
            return;
        }
        
        let tz = timezoneComp.getValue();

        let data = {
            "cert": selectedCertValue,
            "dkdm": selectedDKDMValue.displayName,
            "startDate": start,
            "endDate": end,
            "timezone": tz,
            "outputDir": outputDir
        }

        showLoading = true;
        coms.submitJSON('/api/kdm/submit', data).then(res => {
            console.log(res.status);
            // updateHistory();
            showLoading = false;
        });
    }
</script>


<main id="main">
    <div class="hidden">
        <LoadingIcon width="30px" height="30px"/>
    </div>
    <ErrorModal bind:this={errorModal} on:click={closeError}/>
    <HeroSection navLinks={navLinks}>
        <div class="certSection">
            <div style="width: 40%">
                <SearchList listData={certData}
                    on:fileAdded={test}
                    bind:selected={selectedCertValue}
                    header="Certificate"
                    boxHeight="200px"
                    searchPlaceholder="Search Certs"
                    fileIcon={CertificateIcon}
                    dirIcon={FolderIcon}
                />
                <Selected bind:this={selectedCertElem} selected={selectedCertValue}/>
            </div>
            <div style="width: 40%">
                <SearchList listData={dkdmData}
                    bind:selected={selectedDKDMValue}
                    header="CPL DKDM"
                    boxHeight="200px"
                    searchPlaceholder="Search CPLs"
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
                <div>
                    {#if showLoading}
                        <LoadingIcon width="30px" height="30px"/>
                    {:else}
                        <ImportantBtn
                            on:click={submit}
                            content="Generate"
                            fontSize="12pt"
                            padding="10px 150px"
                        />
                    {/if}
                </div>
            </div>
        </div>
    </section>
    <FooterLinks navLinks={navLinks} paddingTop="50px" showBorder={false}/>
</main>

<style>
    main {
        font-family: "Montserrat";
        position: relative;
        min-width: 900px;
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
        width: 800px;
        padding: 5px;
        gap: 10px
    }

    .hidden {
        display: none;
    }
</style>