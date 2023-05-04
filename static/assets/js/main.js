
// removeAllChildren and str2ab and importPrivateKey cribbed from stack overflow and mozilla example code
async function removeAllChildren(node) {
	while (node.firstChild) {
		node.removeChild(node.lastChild);
	}
}

async function str2ab(str) {
  const buf = new ArrayBuffer(str.length);
  const bufView = new Uint8Array(buf);
  for (let i = 0, strLen = str.length; i < strLen; i++) {
    bufView[i] = str.charCodeAt(i);
  }
  return buf;
}

async function importPrivateKey(pem) {
  // fetch the part of the PEM string between header and footer
  const pemHeader = "-----BEGIN PRIVATE KEY-----";
  const pemFooter = "-----END PRIVATE KEY-----";
  const pemContents = pem.substring(
    pemHeader.length,
    pem.length - pemFooter.length
  );
	console.log(pemContents);
  // base64 decode the string to get the binary data
  const binaryDerString = window.atob(pemContents.replace(/\s/g, '').replace(/(\s)[ \t]+/g, '$1'));
  // convert from a binary string to an ArrayBuffer
  const binaryDer = await str2ab(binaryDerString);
  const result = await window.crypto.subtle.importKey(
    "pkcs8",
    binaryDer,
    {
      name: "RSASSA-PKCS1-v1_5",
      hash: "SHA-256",
    },
    true,
    ["sign"]
  );
	return result;
}

function _arrayBufferToBase64( buffer ) {
    var binary = '';
    var bytes = new Uint8Array( buffer );
    var len = bytes.byteLength;
    for (var i = 0; i < len; i++) {
        binary += String.fromCharCode( bytes[ i ] );
    }
    return window.btoa( binary );
}

async function sign(private_key, data) {
	private_key = await importPrivateKey(private_key);
	let data_buf = await str2ab(data);
	const result = await crypto.subtle.sign("RSASSA-PKCS1-v1_5", private_key, data_buf);
	return _arrayBufferToBase64(result);
}


async function getCurrentNodes() {
	let endpoint = "https://ransom.isis.vanderbilt.edu/alex_richardson_no_touchy/blockchain_project/get_current_nodes.php";
	let node_name = document.getElementById("nodes").value;
  const response = await fetch(endpoint, { method: 'GET'});
  return await response.json();
}

async function refresh_nodes() {
	let node_entries = await getCurrentNodes();
	let node_box = document.getElementById("nodes");
	await removeAllChildren(node_box);
	for (const entry of node_entries) {
		new_option = document.createElement("option");
		new_option.value = entry;
		new_option.innerHTML = entry;
		node_box.appendChild(new_option);
		node_box.value = entry;
	}
}

async function getCurrentUsers() {
	let endpoint = "https://ransom.isis.vanderbilt.edu/alex_richardson_no_touchy/blockchain_project/get_current_users.php?";
	let node_name = document.getElementById("nodes").value;
  const response = await fetch(endpoint + new URLSearchParams({
    node_name: node_name
	}), { method: 'GET'});
  return await response.json();
}

async function generateUserTableEntry(table, username, decryption_key) {
	let row = document.createElement("tr");
	let column1 = document.createElement("th");
	let column2 = document.createElement("th");
	column1.innerHTML = username;
	column2.innerHTML = decryption_key;
	row.appendChild(column1);
	row.appendChild(column2);
	table.appendChild(row);
}

async function refresh_users() {
	let current_users = await getCurrentUsers();
	let user_table = document.getElementById("user_list");
	await removeAllChildren(user_table);
	await generateUserTableEntry(user_table, "Username", "Decryption (public) key");
	for (const entry of current_users) {
		await generateUserTableEntry(user_table, entry.username, entry.public_key);
	}
}

async function AddUserRequest(username, public_key) {
	let endpoint = "https://ransom.isis.vanderbilt.edu/alex_richardson_no_touchy/blockchain_project/add_user.php?";
	let node_name = document.getElementById("nodes").value;
  const response = await fetch(endpoint + new URLSearchParams({
    username: username,
    public_key: public_key,
		node_name: node_name
  }), { method: 'GET'});
  const result_json = await response.json();
	return result_json["response"];
}

async function add_user() {
	let username_tag = document.getElementById("username");
	let public_key_tag = document.getElementById("public_key");
	let username_text = username_tag.value;
	let public_key_text = public_key_tag.value;
	let result = await AddUserRequest(username_text, public_key_text);
	console.log(username_text);
	console.log(public_key_text);
	console.log(result);
	if (result) {
		console.log("User addition successful!");
	}
	else {
		console.log("User addition failed!");
	}
}

async function getCurrentElections() {
	let endpoint = "https://ransom.isis.vanderbilt.edu/alex_richardson_no_touchy/blockchain_project/get_current_elections.php?";
	let node_name = document.getElementById("nodes").value;
  const response = await fetch(endpoint + new URLSearchParams({
    node_name: node_name
	}), { method: 'GET'});
  return await response.json();
}

async function generateElectionTableEntry(table, name, prompt, user, yays, nays) {
	let row = document.createElement("tr");
	let column1 = document.createElement("th");
	let column2 = document.createElement("th");
	let column3 = document.createElement("th");
	let column4 = document.createElement("th");
	let column5 = document.createElement("th");

	column1.innerHTML = name;
	column2.innerHTML = prompt;
	column3.innerHTML = user;
	column4.innerHTML = yays;
	column5.innerHTML = nays;
	row.appendChild(column1);
	row.appendChild(column2);
	row.appendChild(column3);
	row.appendChild(column4);
	row.appendChild(column5);
	table.appendChild(row);
}

async function refresh_elections() {
	let elections = await getCurrentElections();
	let election_table = document.getElementById("election_list");
	await removeAllChildren(election_table);
	await generateElectionTableEntry(election_table, "Election name", "Election prompt", "User", "Yes count", "No count");
	for (const entry of elections) {
			await generateElectionTableEntry(election_table, entry.name, entry.prompt, entry.username, entry.yays.toString(), entry.nays.toString());
	}
}

async function AddElectionRequest(name, prompt, username, private_key) {
	let endpoint = "https://ransom.isis.vanderbilt.edu/alex_richardson_no_touchy/blockchain_project/add_election.php?";
	let node_name = document.getElementById("nodes").value;
	let signature = await sign(private_key, name + prompt + username);

  const response = await fetch(endpoint + new URLSearchParams({
    name: name,
    prompt: prompt,
		username: username,
		signature: signature,
		node_name: node_name
  }), { method: 'GET'});
  const result_json = await response.json();
	return result_json["response"];
}

async function submit_election() {
	let election_name_tag = document.getElementById("election_name");
	let election_prompt_tag = document.getElementById("election_prompt");
	let election_username_tag = document.getElementById("election_username");
	let election_private_key_tag = document.getElementById("election_private_key");

	let election_name = election_name_tag.value;
	let election_prompt = election_prompt_tag.value;
	let election_username = election_username_tag.value;
	let election_private_key = election_private_key_tag.value;

	console.log(election_name, election_prompt, election_username, election_private_key);
	if (await AddElectionRequest(election_name, election_prompt, election_username, election_private_key)) {
		console.log("Election addition successful!");
	}
	else {
		console.log("Election addition failed!");
	}
}

async function AddVoteRequest(name, username, private_key, vote) {
	let endpoint = "https://ransom.isis.vanderbilt.edu/alex_richardson_no_touchy/blockchain_project/add_vote.php?";
	let node_name = document.getElementById("nodes").value;
	let signature = await sign(private_key, name + username + vote);

  const response = await fetch(endpoint + new URLSearchParams({
    name: name,
    username: username,
		vote: vote,
		signature: signature,
		node_name: node_name
  }), { method: 'GET'});
  const result_json = await response.json();
	return result_json["response"];
}

async function submit_vote() {
	let vote_election_name_tag = document.getElementById("election_vote_name");
	let vote_election_username_tag = document.getElementById("election_vote_username");
	let vote_election_private_key_tag = document.getElementById("election_vote_private_key");
	let vote_election_choices = document.getElementsByName("vote_value");
	let vote_choice = null;
	for (const entry of vote_election_choices) {
		if (entry.checked) {
			vote_choice = entry.value;
		}
	}
	let vote_election_name = vote_election_name_tag.value;
	let vote_election_username = vote_election_username_tag.value;
	let vote_election_private_key = vote_election_private_key_tag.value;
	console.log(vote_election_name, vote_election_username, vote_election_private_key, vote_choice);
	if (await AddVoteRequest(vote_election_name, vote_election_username, vote_election_private_key, vote_choice)) {
		console.log("Vote addition successful!");
	}
	else {
		console.log("Vote addition failed!");
	}
}
