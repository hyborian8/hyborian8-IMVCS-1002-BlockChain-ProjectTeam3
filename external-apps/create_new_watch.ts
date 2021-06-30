import { Gateway, Wallets } from 'fabric-network';
import * as path from 'path';
import * as fs from 'fs';

process.argv.forEach((val, index) => {
 // console.log(`${index}: ${val}`)
})

//const args = require('minimist')(process.argv.slice(2))
const args = process.argv.slice(2)
//console.log(args[0])
//console.log(args[1])
//console.log(args[2])
//console.log(args[3])
//console.log(args[4])

async function main() {
  try {

    // Create a new file system based wallet for managing identities.
    const walletPath = path.join(process.cwd(), 'Org1Wallet');
    const wallet = await Wallets.newFileSystemWallet(walletPath);
    //console.log(`Wallet path: ${walletPath}`);

    // Create a new gateway for connecting to our peer node.
    const gateway = new Gateway();
    const connectionProfilePath = path.resolve(__dirname, '..', 'connection.json');
    const connectionProfile = JSON.parse(fs.readFileSync(connectionProfilePath, 'utf8')); // eslint-disable-line @typescript-eslint/no-unsafe-assignment
    const connectionOptions = { wallet, identity: 'Org1 Admin', discovery: { enabled: true, asLocalhost: true } };
    await gateway.connect(connectionProfile, connectionOptions);

    // Get the network (channel) our contract is deployed to.
    const network = await gateway.getNetwork('mychannel');

    // Get the contract from the network.
    const contract = network.getContract('chrono-contract');

    const arrdata = fs.readFileSync('myfile', 'utf8').split('@');
    //console.log(arrdata[0])
    //console.log(arrdata[1])

    // Submit the specified transaction.
    const result = await contract.submitTransaction('RegisterMyWatch', arrdata[0], arrdata[1], arrdata[2], arrdata[3], arrdata[4], arrdata[5], arrdata[6], arrdata[7]);
    console.log(`Transaction has been submitted.`);


    // Disconnect from the gateway.
    gateway.disconnect();
    process.exit()

  } catch (error) {
    console.error('Failed to submit transaction:',error);
    process.exit(1);
  }
}
void main();