/*
 * SPDX-License-Identifier: Apache-2.0
 */

import { Object, Property } from 'fabric-contract-api';

@Object()
export class ChronoLedger {

    @Property()
    public AuthDealer: string; 
    public Brand: string;  
    public Model: string;
    public SerialNo: string;
    public PurchaseDate: string;
    public CertifiedBy: string;
    public CertifiedDate: string;
    public Owner: string;
    public OwnershipDate: string;
    public Status: string;
    public StatusDateTime: string;
    static Brand: string;

}
